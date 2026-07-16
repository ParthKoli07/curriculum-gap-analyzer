"""
main.py
-------
Pipeline orchestrator for Curriculum Gap Analyzer.
Ties together preprocessing, gap analysis, and recommendations
into a single end-to-end pipeline.

Author: Parth Koli
College: Satish Pradhan Dnyanasadhana College, Thane
Project: Curriculum Gap Analyzer (Final Year Project 2026-27)
"""

import os
from app.matcher import compute_gap, print_gap_summary
from app.recommender import recommend_for_gaps, print_recommendations

def run_analysis(top_n_skills=300, top_n_recommendations=10, syllabus_text=None):
    """Run the full curriculum gap analysis pipeline"""

    if not os.path.exists('data/syllabus.txt') and syllabus_text is None:
        print("Error: No syllabus found!")
        return None, None

    print("\n" + "="*60)
    print("   CURRICULUM GAP ANALYZER")
    print("   Powered by NLP & LinkedIn Job Data")
    print("="*60)

    # Step 1: Run gap analysis
    print("\n[1/3] Running gap analysis...")
    df_report = compute_gap(top_n_skills=top_n_skills, syllabus_text=syllabus_text)

    if df_report is None:
        print("Error: Could not generate gap report.")
        return None, None

    # Step 2: Print gap summary
    print("\n[2/3] Generating gap summary...")
    gaps, covered = print_gap_summary(df_report)

    # Step 3: Get recommendations
    print("\n[3/3] Fetching learning resources...")
    recommendations = recommend_for_gaps(df_report, top_n=top_n_recommendations)
    print_recommendations(recommendations)

    print("\n✅ Analysis complete!\n")
    return df_report, recommendations

if __name__ == "__main__":
    run_analysis(top_n_skills=300, top_n_recommendations=10)