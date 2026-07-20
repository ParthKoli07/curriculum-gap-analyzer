"""
preprocess.py
-------------
Data loading and preprocessing module for Curriculum Gap Analyzer.

Loads the pre-filtered CS/tech jobs dataset from Hugging Face,
extracts job-market skills, cleans text, and loads syllabus content.

Author: Parth Koli
College: Satish Pradhan Dnyanasadhana College, Thane
Project: Curriculum Gap Analyzer (Final Year Project 2026-27)
"""

import pandas as pd
import re
from collections import Counter
from datasets import load_dataset


# Hugging Face dataset repository
DATASET_ID = "T1METURNER/tech-jobs-dataset"


def load_tech_job_data():
    """
    Load the pre-filtered CS/tech jobs dataset from Hugging Face.

    The dataset already contains only technology-related job postings,
    so no additional job-title filtering or dataset merging is required.

    Returns:
        pandas.DataFrame: DataFrame containing:
            - job_link
            - job_skills
            - job_title
            - company
    """
    print("Loading tech jobs dataset from Hugging Face...")

    try:
        dataset = load_dataset(DATASET_ID, split="train")
        df = dataset.to_pandas()

        print(f"Loaded {len(df)} tech job records.")
        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        return pd.DataFrame()


def clean_text(text):
    """
    Clean and normalize text.

    Converts text to lowercase, removes special characters,
    and removes unnecessary whitespace.
    """
    if pd.isna(text):
        return ""

    text = str(text).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def extract_skills_list(df):
    """
    Extract and count skills from job postings.

    Args:
        df (pandas.DataFrame): Job dataset containing a
        'job_skills' column.

    Returns:
        Counter: Skill names and their occurrence counts.
    """
    all_skills = []

    if df.empty:
        return Counter()

    if "job_skills" not in df.columns:
        print("Error: 'job_skills' column not found in dataset.")
        return Counter()

    for skills_str in df["job_skills"].dropna():

        # Remove brackets and quotation marks if present
        skills_str = re.sub(r"[\[\]']", "", str(skills_str))

        # Split comma-separated skills
        skills = [
            skill.strip().lower()
            for skill in skills_str.split(",")
            if skill.strip()
        ]

        all_skills.extend(skills)

    return Counter(all_skills)


def load_syllabus(syllabus_path="data/syllabus.txt"):
    """
    Load and clean syllabus content from a text file.

    Args:
        syllabus_path (str): Path to the syllabus text file.

    Returns:
        str: Cleaned syllabus text.
    """
    try:
        with open(syllabus_path, "r", encoding="utf-8") as file:
            content = file.read()

        return clean_text(content)

    except FileNotFoundError:
        print(f"Syllabus file not found at {syllabus_path}")
        return ""

def get_skills_for_role(role_keyword,
                         skills_path='data/tech_jobs_filtered.csv'):
    """Get top skills for a specific job role"""
    from collections import Counter
    
    print(f"Loading skills for role: {role_keyword}...")
    
    # Try local file first, fall back to HuggingFace
    try:
        df = pd.read_csv(skills_path)
        print(f"Loaded from local file")
    except FileNotFoundError:
        print(f"Local file not found, loading from HuggingFace...")
        from datasets import load_dataset
        dataset = load_dataset('T1METURNER/tech-jobs-dataset')
        df = pd.DataFrame(dataset['train'])
        print(f"Loaded from HuggingFace")
    
    # Filter by role keyword
    role_df = df[
        df['job_title'].str.lower().str.contains(role_keyword.lower(), na=False)
    ]
    
    print(f"Found {len(role_df)} job postings for '{role_keyword}'")
    
    if len(role_df) == 0:
        return {}
    
    # Extract skills
    all_skills = []
    for skills_str in role_df['job_skills'].dropna():
        skills_str = re.sub(r"[\[\]']", '', str(skills_str))
        skills = [s.strip().lower() for s in skills_str.split(',') if s.strip()]
        all_skills.extend(skills)
    
    skill_counts = Counter(all_skills)
    return dict(skill_counts)