import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

STOP_WORDS = set(stopwords.words('english'))

def load_job_data(skills_path='data/job_skills.csv', 
                  postings_path='data/linkedin_job_postings.csv'):
    """Load and merge job skills with job postings"""
    print("Loading datasets...")
    
    skills_df = pd.read_csv(skills_path)
    postings_df = pd.read_csv(postings_path, usecols=['job_link', 'job_title', 'company'])
    
    # Merge on job_link
    merged_df = pd.merge(skills_df, postings_df, on='job_link', how='inner')
    print(f"Loaded {len(merged_df)} job records after merging.")
    return merged_df

def clean_text(text):
    """Clean and normalize text"""
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_skills_list(merged_df):
    """Extract all unique skills from job postings"""
    all_skills = []
    for skills_str in merged_df['job_skills'].dropna():
        # Skills are stored as a list-like string e.g. "['Python', 'SQL']"
        skills_str = re.sub(r"[\[\]']", '', str(skills_str))
        skills = [s.strip().lower() for s in skills_str.split(',') if s.strip()]
        all_skills.extend(skills)
    
    # Get unique skills and their frequency
    from collections import Counter
    skill_counts = Counter(all_skills)
    return skill_counts

def load_syllabus(syllabus_path='data/syllabus.txt'):
    """Load syllabus content from a text file"""
    try:
        with open(syllabus_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return clean_text(content)
    except FileNotFoundError:
        print(f"Syllabus file not found at {syllabus_path}")
        return ""

if __name__ == "__main__":
    df = load_job_data()
    print(df.head())
    print("\nSample skills:")
    skill_counts = extract_skills_list(df)
    print(dict(list(skill_counts.most_common(20))))