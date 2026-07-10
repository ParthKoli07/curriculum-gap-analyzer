import streamlit as st
import pandas as pd
from app.main import run_analysis

st.set_page_config(
    page_title="Curriculum Gap Analyzer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Curriculum Gap Analyzer")
st.markdown("### Compares your college syllabus against industry job requirements")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    top_n = st.slider("Number of skills to analyze", 
                       min_value=50, max_value=500, value=300, step=50)
    top_recs = st.slider("Number of gap recommendations", 
                          min_value=5, max_value=20, value=10, step=5)
    run_btn = st.button("🚀 Run Analysis", use_container_width=True)

if run_btn:
    with st.spinner("Running analysis... this may take a minute ⏳"):
        df_report, recommendations = run_analysis(
            top_n_skills=top_n, 
            top_n_recommendations=top_recs
        )

    # Summary metrics
    gaps = df_report[df_report['is_gap'] == True]
    covered = df_report[df_report['is_gap'] == False]
    coverage_pct = round(len(covered) / len(df_report) * 100, 1)

    st.markdown("## 📊 Analysis Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Skills Analyzed", len(df_report))
    col2.metric("Skills Covered", len(covered))
    col3.metric("Skill Gaps Found", len(gaps))
    col4.metric("Coverage %", f"{coverage_pct}%")

    st.markdown("---")

    # Two columns layout
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### ❌ Top Skill Gaps")
        st.markdown("*High industry demand but missing from syllabus*")
        gap_display = gaps[['skill', 'industry_frequency']].head(15).reset_index(drop=True)
        gap_display.columns = ['Skill', 'Industry Demand']
        st.dataframe(gap_display, use_container_width=True)

    with col_right:
        st.markdown("### ✅ Skills Covered in Syllabus")
        st.markdown("*Already present in your curriculum*")
        covered_display = covered[['skill', 'industry_frequency']].head(15).reset_index(drop=True)
        covered_display.columns = ['Skill', 'Industry Demand']
        st.dataframe(covered_display, use_container_width=True)

    st.markdown("---")

    # Bar chart of top gaps
    st.markdown("### 📈 Top 10 Skill Gaps by Industry Demand")
    chart_data = gaps[['skill', 'industry_frequency']].head(10).set_index('skill')
    chart_data.columns = ['Industry Demand']
    st.bar_chart(chart_data)

    st.markdown("---")

    # Recommendations
    st.markdown("### 🎯 Free Learning Resources for Your Gaps")
    for i, rec in enumerate(recommendations, 1):
        with st.expander(f"{i}. {rec['skill'].upper()} — Industry Demand: {rec['industry_frequency']}"):
            for resource in rec['resources']:
                st.markdown(f"**📚 {resource['title']}**")
                st.markdown(f"Platform: `{resource['platform']}`")
                st.markdown(f"🔗 [Open Course]({resource['url']})")
                st.markdown("---")

    # Download report
    st.markdown("---")
    st.markdown("### 💾 Download Full Report")
    csv = df_report.to_csv(index=False)
    st.download_button(
        label="⬇️ Download Gap Report as CSV",
        data=csv,
        file_name="curriculum_gap_report.csv",
        mime="text/csv",
        use_container_width=True
    )

else:
    st.info("👈 Click **Run Analysis** in the sidebar to start!")
    st.markdown("### How it works:")
    st.markdown("""
    1. 📄 Loads your college syllabus from `data/syllabus.txt`
    2. 💼 Analyzes 32,000+ real tech job postings from LinkedIn
    3. 🔍 Compares skills demanded by industry vs what your syllabus covers
    4. 📊 Shows you exactly what to self-learn before placements
    5. 🎯 Recommends free courses for each skill gap
    """)