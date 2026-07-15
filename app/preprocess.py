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


if __name__ == "__main__":

    # Load tech jobs from Hugging Face
    df = load_tech_job_data()

    if not df.empty:

        print("\nDataset preview:")
        print(df.head())

        print("\nDataset columns:")
        print(df.columns.tolist())

        print("\nTop 20 most common tech skills:")

        skill_counts = extract_skills_list(df)

        for skill, count in skill_counts.most_common(20):
            print(f"{skill}: {count}")

    else:
        print("No job data was loaded.")