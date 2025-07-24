import json
import os
import sys

def generate_report(subject):
    """Generates a performance report for a given subject."""
    results_path = os.path.join("results", f"{subject}_results.jsonl")
    report_path = os.path.join("results", f"{subject}_report.md")

    if not os.path.exists(results_path):
        print(f"Error: Results file for subject '{subject}' not found at {results_path}")
        return

    with open(results_path, 'r') as f:
        results = [json.loads(line) for line in f]

    total = len(results)
    correct = sum(1 for r in results if r['is_correct'])
    accuracy = (correct / total) * 100 if total > 0 else 0

    # Analyze errors
    error_examples = []
    for res in results:
        if not res['is_correct']:
            error_examples.append(
                f"- **Question ID:** {res['question_id']}\n"
                f"  - **Question:** {res['question']}\n"
                f"  - **Choices:** {res['choices']}\n"
                f"  - **Correct Answer:** {res['correct_answer_index']}\n"
                f"  - **My Answer:** {res['agi_answer_index']}\n"
                f"  - **Reasoning Trace:**\n```lisp\n{res['reasoning_trace']}\n```"
            )
        if len(error_examples) == 5: # Limit to 5 examples for brevity
            break

    # Generate report
    report_content = f"""# MMLU Cognitive Ability Report: {subject.replace('_', ' ').title()}

---

### 1. Overall Performance

*   **Subject:** {subject}
*   **Total Questions:** {total}
*   **Correct Answers:** {correct}
*   **Accuracy:** {accuracy:.2f}%

### 2. Performance Analysis

The current performance is based on a baseline model (`test_runner.py`) that uses a naive 'select the first option' heuristic. This establishes a performance floor and is not representative of the full cognitive capabilities of BaseAGI. The accuracy of {accuracy:.2f}% is close to the random chance baseline of 25% for four-choice questions.

### 3. Error Analysis (Sample of 5 Errors)

This section highlights specific examples where the baseline model failed. The 'Reasoning Trace' shows the simplistic, non-cognitive path taken. Future iterations will replace this with a full RR-Tree analysis.

{"\n".join(error_examples)}

### 4. Path to Improvement

1.  **Implement Real Cognition:** The next critical step is to replace the `run_base_agi_cognition` placeholder in `test_runner.py` with a genuine call to the BaseAGI model. This will involve:
    *   Passing the question and choices to the model.
    *   Executing the full Observe-Guess-Understand-Practice-Learn workflow.
    *   Using the KIRP protocol to query the CPIL for relevant knowledge (even if initially empty).
    *   Returning the final, reasoned answer and the complete RR-Tree as the reasoning trace.
2.  **Iterative Testing:** Re-run the benchmark for `abstract_algebra` with the real cognitive model to establish a new, more meaningful performance baseline.
3.  **Knowledge Integration:** For subjects where performance is low, analyze the error patterns in the RR-Tree traces to identify knowledge gaps. Create new knowledge modules (`.md` files) for the CPIL that codify the missing concepts or reasoning strategies.
4.  **Incremental Expansion:** Continue this process for all subjects in the `mmlu_subjects` list, gradually building both the test coverage and the cognitive capabilities of the AGI.
"""

    with open(report_path, 'w') as f:
        f.write(report_content)

    print(f"Successfully generated report for {subject} at {report_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_report.py <subject_name>")
    else:
        generate_report(sys.argv[1])
