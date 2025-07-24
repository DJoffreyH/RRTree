import json
import os
import sys
from datasets import load_from_disk

import re

def run_base_agi_cognition(question, choices):
    """
    Simulates an evolved BaseAGI reasoning process using keyword matching.
    """
    # A simple set of common English stop words.
    stop_words = {'a', 'an', 'the', 'in', 'on', 'is', 'are', 'of', 'for', 'to', 'and', 'or', 'by', 'with'}

    # Extract keywords from the question, ignoring stop words and short words.
    question_keywords = set(re.findall(r'\b\w+\b', question.lower()))
    question_keywords = {word for word in question_keywords if word not in stop_words and len(word) > 2}

    best_choice_index = 0
    max_score = -1
    
    scores = []
    for i, choice in enumerate(choices):
        choice_keywords = set(re.findall(r'\b\w+\b', choice.lower()))
        score = len(question_keywords.intersection(choice_keywords))
        scores.append(score)
        if score > max_score:
            max_score = score
            best_choice_index = i

    # Build a more detailed reasoning trace
    alternatives_trace = []
    for i, score in enumerate(scores):
        status = "chosen" if i == best_choice_index else "evaluated"
        alternatives_trace.append(
            f"      (option_{i} (status \"{status}\") (score {score}) (reason \"Keyword overlap score.\"))"
        )
    
    reasoning_trace = (
        "(root\n"
        "  (goal \"Answer the multiple-choice question correctly.\")\n"
        "  (problem_analysis\n"
        f"    (question \"{question}\")\n"
        f"    (keywords_extracted {list(question_keywords)})\n"
        f"    (options {choices})\n"
        "  )\n"
        "  (hypothesis_generation\n"
        "    (alternatives\n"
        + "\n".join(alternatives_trace) +
        "\n    ))\n"
        ")"
    )

    return {
        "answer_index": best_choice_index,
        "reasoning_trace": reasoning_trace
    }

def run_test(subject):
    """Runs the MMLU test for a given subject."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)

    dataset_path = os.path.join(base_dir, "data", subject)
    results_path = os.path.join(base_dir, "results", f"{subject}_results.jsonl")

    if not os.path.exists(dataset_path):
        print(f"Error: Dataset for subject '{subject}' not found at {dataset_path}")
        return

    print(f"Loading dataset for {subject}...")
    dataset = load_from_disk(dataset_path)
    test_split = dataset.get('test')

    if not test_split:
        print(f"Error: 'test' split not found for subject '{subject}'. Available splits: {list(dataset.keys())}")
        return

    results = []
    total = len(test_split)
    correct = 0

    print(f"Starting test for {subject}. Total questions: {total}")

    for i, item in enumerate(test_split):
        question = item['question']
        choices = item['choices']
        correct_answer_index = item['answer']

        # Simulate the AGI's cognitive process
        agi_result = run_base_agi_cognition(question, choices)
        
        is_correct = (agi_result["answer_index"] == correct_answer_index)
        if is_correct:
            correct += 1

        result_record = {
            "question_id": i,
            "question": question,
            "choices": choices,
            "correct_answer_index": correct_answer_index,
            "agi_answer_index": agi_result["answer_index"],
            "is_correct": is_correct,
            "reasoning_trace": agi_result["reasoning_trace"]
        }
        results.append(result_record)

        # Print progress
        if (i + 1) % 10 == 0:
            print(f"  ...processed {i + 1}/{total} questions.")

    # Save raw results
    with open(results_path, 'w') as f:
        for res in results:
            f.write(json.dumps(res) + '\n')

    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"Test for {subject} complete.")
    print(f"Accuracy: {accuracy:.2f}% ({correct}/{total})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_runner.py <subject_name>")
    else:
        run_test(sys.argv[1])