import sys
import os
import json
import random
from datasets import load_from_disk

def run_randomized_test(subject, num_questions=10):
    """Loads a subject, randomizes choices, and prints questions for the AGI."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    dataset_path = os.path.join(base_dir, "data", subject)

    if not os.path.exists(dataset_path):
        print(f"Error: Dataset for subject '{subject}' not found.", file=sys.stderr)
        return

    try:
        dataset = load_from_disk(dataset_path)
        test_split = dataset.get('test')
        if not test_split:
            print(f"Error: 'test' split not found for subject '{subject}'.", file=sys.stderr)
            return

        print(f"--- MMLU Randomized Test ---_\nSubject: {subject}\n")

        for i, item in enumerate(test_split):
            if i >= num_questions:
                break

            original_choices = item['choices']
            correct_answer_text = original_choices[item['answer']]

            shuffled_choices = original_choices[:]
            random.shuffle(shuffled_choices)

            new_correct_index = shuffled_choices.index(correct_answer_text)

            # Present the data to the AGI
            print(f"--- Question {i+1}/{num_questions} ---")
            print(f"Question: {item['question']}")
            print(f"Choices: {json.dumps(shuffled_choices)}")
            print(f"Correct Answer Index (for verification): {new_correct_index}")
            print(f"Original Correct Answer Text: {correct_answer_text}\n")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python randomized_tester.py <subject_name> [num_questions]", file=sys.stderr)
    else:
        subject_name = sys.argv[1]
        num_q = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        run_randomized_test(subject_name, num_q)
