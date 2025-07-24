from datasets import load_dataset
import os

def download_mmlu():
    """Downloads the MMLU dataset from Hugging Face and saves it to the data directory."""
    print("Downloading MMLU dataset...")
    
    # Create the data directory if it doesn't exist
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    data_path = os.path.join(base_dir, "data")
    os.makedirs(data_path, exist_ok=True)
    
    # All MMLU subjects
    mmlu_subjects = [
        'abstract_algebra', 'anatomy', 'astronomy', 'business_ethics', 'clinical_knowledge',
        'college_biology', 'college_chemistry', 'college_computer_science', 'college_mathematics',
        'college_medicine', 'college_physics', 'computer_security', 'conceptual_physics',
        'econometrics', 'electrical_engineering', 'elementary_mathematics', 'formal_logic',
        'global_facts', 'high_school_biology', 'high_school_chemistry', 'high_school_computer_science',
        'high_school_european_history', 'high_school_geography', 'high_school_government_and_politics',
        'high_school_macroeconomics', 'high_school_mathematics', 'high_school_microeconomics',
        'high_school_physics', 'high_school_psychology', 'high_school_statistics',
        'high_school_us_history', 'high_school_world_history', 'human_aging', 'human_sexuality',
        'international_law', 'jurisprudence', 'logical_fallacies', 'machine_learning',
        'management', 'marketing', 'medical_genetics', 'miscellaneous', 'moral_disputes',
        'moral_scenarios', 'nutrition', 'philosophy', 'prehistory', 'professional_accounting',
        'professional_law', 'professional_medicine', 'professional_psychology', 'public_relations',
        'security_studies', 'sociology', 'us_foreign_policy', 'virology', 'world_religions'
    ]

    for subject in mmlu_subjects:
        print(f"Downloading {subject}...")
        try:
            dataset = load_dataset("cais/mmlu", subject)
            dataset.save_to_disk(os.path.join(data_path, subject))
            print(f"Successfully downloaded and saved {subject}.")
        except Exception as e:
            print(f"Failed to download {subject}. Error: {e}")

if __name__ == "__main__":
    download_mmlu()
