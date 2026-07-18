"""
resume_parser.py
----------------
Resume parsing module for Curriculum Gap Analyzer.
Extracts skills from uploaded resume PDFs or text files
to personalize the gap analysis per individual student.

Author: Parth Koli
College: Satish Pradhan Dnyanasadhana College, Thane
Project: Curriculum Gap Analyzer (Final Year Project 2026-27)
"""

import re
import PyPDF2
from app.preprocess import clean_text

# Common skills to look for in resumes
SKILL_KEYWORDS = [
    # Programming Languages
    'python', 'java', 'javascript', 'c++', 'c#', 'typescript', 'scala',
    'golang', 'rust', 'php', 'ruby', 'swift', 'kotlin', 'r programming',

    # Web Development
    'react', 'angular', 'vue', 'node.js', 'django', 'flask', 'fastapi',
    'html', 'css', 'bootstrap', 'tailwind', 'next.js', 'express',

    # Data Science & ML
    'machine learning', 'deep learning', 'natural language processing',
    'nlp', 'computer vision', 'data science', 'data analysis',
    'tensorflow', 'pytorch', 'keras', 'scikit-learn', 'pandas', 'numpy',
    'matplotlib', 'seaborn', 'jupyter', 'opencv',

    # Cloud & DevOps
    'aws', 'azure', 'google cloud', 'docker', 'kubernetes', 'jenkins',
    'terraform', 'ansible', 'devops', 'ci/cd', 'linux', 'git',

    # Databases
    'sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite',
    'nosql', 'firebase', 'cassandra', 'elasticsearch',

    # Tools & Platforms
    'tableau', 'power bi', 'jira', 'confluence', 'github', 'gitlab',
    'postman', 'figma', 'unity', 'arduino', 'esp32', 'raspberry pi',

    # AI/GenAI
    'langchain', 'openai', 'huggingface', 'prompt engineering',
    'llm', 'rag', 'vector database', 'pinecone', 'streamlit',

    # Concepts
    'agile', 'scrum', 'rest api', 'graphql', 'microservices',
    'object oriented programming', 'data structures', 'algorithms',
    'software engineering', 'system design', 'cybersecurity',
]

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def extract_text_from_txt(txt_file):
    """Extract text from uploaded TXT file"""
    try:
        return txt_file.read().decode("utf-8")
    except Exception as e:
        print(f"Error reading TXT: {e}")
        return ""

def extract_skills_from_resume(resume_file, file_type):
    """
    Extract skills from a resume file
    Returns a list of detected skills
    """
    # Get text from file
    if file_type == "application/pdf":
        text = extract_text_from_pdf(resume_file)
    else:
        text = extract_text_from_txt(resume_file)

    if not text:
        return []

    # Clean and lowercase
    text_lower = clean_text(text)

    # Find matching skills
    detected_skills = []
    for skill in SKILL_KEYWORDS:
        if skill.lower() in text_lower:
            detected_skills.append(skill.lower())

    return detected_skills

def combine_syllabus_and_resume(syllabus_text, resume_skills):
    """
    Combine syllabus text with resume skills
    to create a unified personal knowledge base
    """
    if not resume_skills:
        return syllabus_text

    resume_text = " ".join(resume_skills)
    combined = syllabus_text + " " + resume_text
    return combined