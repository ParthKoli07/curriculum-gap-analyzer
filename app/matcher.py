import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.preprocess import load_job_data, extract_skills_list, load_syllabus

SOFT_SKILLS = {
    'communication', 'customer service', 'teamwork', 'leadership',
    'problem solving', 'time management', 'attention to detail',
    'problemsolving', 'interpersonal skills', 'collaboration',
    'training', 'organizational skills', 'multitasking', 'adaptability',
    'critical thinking', 'creativity', 'work ethic', 'flexibility',
    'conflict resolution', 'decision making', 'emotional intelligence',
    'negotiation', 'presentation skills', 'public speaking', 'mentoring',
    'coaching', 'customer satisfaction', 'patient care', 'nursing',
    'sales', 'inventory management', 'cash handling', 'merchandising',
    'food safety', 'customer relations', 'scheduling', 'budgeting',
    'communication skills', 'interpersonal communication', 'detail oriented',
    'microsoft office suite', 'microsoft office', 'written communication',
    'verbal communication', 'active listening', 'team player',
    'training and development', 'attention to detail', 'time management',
    'high school diploma', 'bachelors degree', 'masters degree',
    'paid time off', 'health insurance', 'dental insurance',
    'supervision', 'safety', 'analytical skills', 'problemsolving skills',
    'troubleshooting', 'excel', 'quality control', 'research',
    '401k', 'vision insurance', 'employee discount', 'referral program',
    'background check', 'drug test', 'drivers license', 'forklift',
    'bilingual', 'physical demands', 'lifting', 'standing',
    'organization', 'management', 'assessment', 'documentation',
    'engineering', 'operations', 'reporting', 'compliance',
    'recruitment', 'onboarding', 'payroll', 'benefits administration'
}
from app.preprocess import load_tech_job_data, extract_skills_list, load_syllabus

def get_industry_skills(top_n=300):
    """Get top N technical skills from tech job postings only"""
    df = load_tech_job_data()  # changed from load_job_data
    skill_counts = extract_skills_list(df)

    filtered_skills = {}
    for skill, count in skill_counts.most_common(1000):
        if skill.lower() not in SOFT_SKILLS and len(skill) > 2:
            filtered_skills[skill] = count
        if len(filtered_skills) >= top_n:
            break

    return filtered_skills

def compute_gap(top_n_skills=300):
    """Compare industry skills vs syllabus content"""
    print("Fetching top industry skills...")
    industry_skills = get_industry_skills(top_n=top_n_skills)

    print("Loading syllabus...")
    syllabus_text = load_syllabus()

    if not syllabus_text:
        print("Error: Syllabus file not found!")
        return None

    skill_names = list(industry_skills.keys())
    skill_freq = list(industry_skills.values())

    # Check direct keyword match instead of TF-IDF
    gap_report = []
    syllabus_lower = syllabus_text.lower()

    for i, skill in enumerate(skill_names):
        # Direct substring match
        is_covered = skill.lower() in syllabus_lower
        
        gap_report.append({
            'skill': skill,
            'industry_frequency': skill_freq[i],
            'in_syllabus': is_covered,
            'is_gap': not is_covered
        })

    df_report = pd.DataFrame(gap_report)
    df_report = df_report.sort_values('industry_frequency', ascending=False)

    return df_report

def print_gap_summary(df_report):
    """Print a clean summary of the gap analysis"""
    gaps = df_report[df_report['is_gap'] == True]
    covered = df_report[df_report['is_gap'] == False]

    print("\n" + "="*60)
    print("CURRICULUM GAP ANALYSIS REPORT")
    print("="*60)
    print(f"Total industry skills analyzed: {len(df_report)}")
    print(f"Skills covered in syllabus:     {len(covered)}")
    print(f"Skills NOT in syllabus (gaps):  {len(gaps)}")
    print(f"Coverage percentage:            {round(len(covered)/len(df_report)*100, 1)}%")

    print("\n TOP 10 SKILL GAPS (High demand, not in syllabus):")
    print("-"*60)
    top_gaps = gaps.head(10)
    for _, row in top_gaps.iterrows():
        print(f"  ❌ {row['skill']:<35} | Freq: {row['industry_frequency']:>6}")

    print("\n TOP 10 SKILLS COVERED IN SYLLABUS:")
    print("-"*60)
    top_covered = covered.head(10)
    for _, row in top_covered.iterrows():
        print(f"  ✅ {row['skill']:<35} | Freq: {row['industry_frequency']:>6}")

    return gaps, covered

if __name__ == "__main__":
    df_report = compute_gap(top_n_skills=300)
    if df_report is not None:
        gaps, covered = print_gap_summary(df_report)
        df_report.to_csv('data/gap_report.csv', index=False)
        print("\n Full report saved to data/gap_report.csv")