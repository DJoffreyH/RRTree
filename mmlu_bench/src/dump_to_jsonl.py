import sys
import os
import json
from datasets import load_from_disk

def dump_subject_to_jsonl(subject):
    """Loads a subject from disk and prints its test split to stdout as JSONL."""
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

        for item in test_split:
            print(json.dumps(item))
            
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dump_to_jsonl.py <subject_name>", file=sys.stderr)
    else:
        dump_subject_to_jsonl(sys.argv[1])
