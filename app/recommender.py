# Free learning resources mapped to common tech skills
RESOURCE_MAP = {
    # Programming Languages
    'python': [
        {'title': 'Python for Everybody', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/specializations/python'},
        {'title': 'Python Tutorial', 'platform': 'W3Schools', 'url': 'https://www.w3schools.com/python/'},
    ],
    'javascript': [
        {'title': 'JavaScript Algorithms and Data Structures', 'platform': 'freeCodeCamp', 'url': 'https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/'},
        {'title': 'JavaScript Tutorial', 'platform': 'W3Schools', 'url': 'https://www.w3schools.com/js/'},
    ],
    'sql': [
        {'title': 'SQL for Data Science', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/learn/sql-for-data-science'},
        {'title': 'SQL Tutorial', 'platform': 'W3Schools', 'url': 'https://www.w3schools.com/sql/'},
    ],
    'java': [
        {'title': 'Java Programming and Software Engineering', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/specializations/java-programming'},
        {'title': 'Java Tutorial', 'platform': 'W3Schools', 'url': 'https://www.w3schools.com/java/'},
    ],
    'c++': [
        {'title': 'C++ Tutorial for Beginners', 'platform': 'YouTube (freeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=vLnPwxZdW4Y'},
    ],

    # Data Science & ML
    'machine learning': [
        {'title': 'Machine Learning Specialization', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/specializations/machine-learning-introduction'},
        {'title': 'Machine Learning Crash Course', 'platform': 'Google', 'url': 'https://developers.google.com/machine-learning/crash-course'},
    ],
    'data science': [
        {'title': 'IBM Data Science Professional Certificate', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/professional-certificates/ibm-data-science'},
        {'title': 'Data Science Fundamentals', 'platform': 'NPTEL', 'url': 'https://nptel.ac.in/courses/106/106/106106212/'},
    ],
    'deep learning': [
        {'title': 'Deep Learning Specialization', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/specializations/deep-learning'},
        {'title': 'Practical Deep Learning', 'platform': 'fast.ai', 'url': 'https://www.fast.ai/'},
    ],
    'natural language processing': [
        {'title': 'NLP Specialization', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/specializations/natural-language-processing'},
    ],
    'tensorflow': [
        {'title': 'TensorFlow Developer Certificate', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/professional-certificates/tensorflow-in-practice'},
    ],
    'pytorch': [
        {'title': 'PyTorch Tutorials', 'platform': 'Official PyTorch', 'url': 'https://pytorch.org/tutorials/'},
    ],

    # Cloud & DevOps
    'aws': [
        {'title': 'AWS Cloud Practitioner Essentials', 'platform': 'AWS Training (Free)', 'url': 'https://aws.amazon.com/training/learn-about/cloud-practitioner/'},
        {'title': 'AWS Fundamentals', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/specializations/aws-fundamentals'},
    ],
    'docker': [
        {'title': 'Docker Tutorial for Beginners', 'platform': 'YouTube (TechWorld with Nana)', 'url': 'https://www.youtube.com/watch?v=3c-iBn73dDE'},
        {'title': 'Docker Getting Started', 'platform': 'Official Docker Docs', 'url': 'https://docs.docker.com/get-started/'},
    ],
    'kubernetes': [
        {'title': 'Kubernetes for Beginners', 'platform': 'YouTube (TechWorld with Nana)', 'url': 'https://www.youtube.com/watch?v=X48VuDVv0do'},
    ],
    'cloud computing': [
        {'title': 'Cloud Computing Basics', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/learn/cloud-computing-basics'},
        {'title': 'Cloud Computing', 'platform': 'NPTEL', 'url': 'https://nptel.ac.in/courses/106/105/106105167/'},
    ],
    'devops': [
        {'title': 'DevOps Beginners to Advanced', 'platform': 'YouTube (freeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=j5Zsa_eOXeY'},
    ],

    # Web Development
    'react': [
        {'title': 'React - The Complete Guide', 'platform': 'YouTube (Academind)', 'url': 'https://www.youtube.com/watch?v=Ke90Tje7VS0'},
        {'title': 'React Tutorial', 'platform': 'freeCodeCamp', 'url': 'https://www.freecodecamp.org/learn/front-end-development-libraries/'},
    ],
    'node.js': [
        {'title': 'Node.js Tutorial', 'platform': 'YouTube (freeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=RLtyhwFtXQA'},
    ],
    'django': [
        {'title': 'Django Tutorial', 'platform': 'Official Django Docs', 'url': 'https://docs.djangoproject.com/en/stable/intro/tutorial01/'},
    ],

    # Databases
    'mongodb': [
        {'title': 'MongoDB Basics', 'platform': 'MongoDB University (Free)', 'url': 'https://university.mongodb.com/courses/M001/about'},
    ],
    'postgresql': [
        {'title': 'PostgreSQL Tutorial', 'platform': 'postgresqltutorial.com', 'url': 'https://www.postgresqltutorial.com/'},
    ],

    # Cybersecurity
    'cybersecurity': [
        {'title': 'Google Cybersecurity Certificate', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/professional-certificates/google-cybersecurity'},
    ],
    'ethical hacking': [
        {'title': 'Ethical Hacking Full Course', 'platform': 'YouTube (freeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=3Kq1MIfTWCE'},
    ],

    # Tools
    'git': [
        {'title': 'Git and GitHub for Beginners', 'platform': 'YouTube (freeCodeCamp)', 'url': 'https://www.youtube.com/watch?v=RGOj5yH7evk'},
    ],
    'linux': [
        {'title': 'Linux Command Line Basics', 'platform': 'Udacity (Free)', 'url': 'https://www.udacity.com/course/linux-command-line-basics--ud595'},
    ],
    'power bi': [
        {'title': 'Power BI Tutorial', 'platform': 'YouTube (Guy in a Cube)', 'url': 'https://www.youtube.com/c/GuyinaCube'},
    ],
    'tableau': [
        {'title': 'Tableau Public Training', 'platform': 'Tableau (Free)', 'url': 'https://www.tableau.com/learn/training'},
    ],
}

DEFAULT_RESOURCE = [
    {'title': 'Search on NPTEL', 'platform': 'NPTEL', 'url': 'https://nptel.ac.in/'},
    {'title': 'Search on Coursera', 'platform': 'Coursera (Free Audit)', 'url': 'https://www.coursera.org/'},
    {'title': 'Search on YouTube', 'platform': 'YouTube', 'url': 'https://www.youtube.com/'},
]

def get_resources(skill):
    """Get free learning resources for a given skill"""
    skill_lower = skill.lower().strip()
    
    # Direct match
    if skill_lower in RESOURCE_MAP:
        return RESOURCE_MAP[skill_lower]
    
    # Partial match
    for key in RESOURCE_MAP:
        if key in skill_lower or skill_lower in key:
            return RESOURCE_MAP[key]
    
    return DEFAULT_RESOURCE

def recommend_for_gaps(gap_df, top_n=10):
    """Generate resource recommendations for top skill gaps"""
    gaps = gap_df[gap_df['is_gap'] == True].head(top_n)
    
    recommendations = []
    for _, row in gaps.iterrows():
        skill = row['skill']
        resources = get_resources(skill)
        recommendations.append({
            'skill': skill,
            'industry_frequency': row['industry_frequency'],
            'resources': resources
        })
    
    return recommendations

def print_recommendations(recommendations):
    """Print recommendations in a readable format"""
    print("\n" + "="*60)
    print("RECOMMENDED FREE RESOURCES FOR SKILL GAPS")
    print("="*60)
    
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec['skill'].upper()} (Demand: {rec['industry_frequency']})")
        print("-"*40)
        for resource in rec['resources']:
            print(f"   📚 {resource['title']}")
            print(f"      Platform: {resource['platform']}")
            print(f"      URL: {resource['url']}")

if __name__ == "__main__":
    from app.matcher import compute_gap
    df_report = compute_gap(top_n_skills=300)
    if df_report is not None:
        recommendations = recommend_for_gaps(df_report, top_n=10)
        print_recommendations(recommendations)