import streamlit as st
import pandas as pd
from app.main import run_analysis

st.set_page_config(
    page_title="Curriculum Gap Analyzer",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .metric-card {
        background-color: #1e1e2e;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .title-text {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
    }
    .subtitle-text {
        font-size: 1.1rem;
        color: #a0aec0;
    }
    .gap-badge {
        background-color: #e53e3e;
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
    }
    .covered-badge {
        background-color: #38a169;
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title-text">📚 Curriculum Gap Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Compares your college syllabus against real industry job requirements to find skill gaps</p>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://img.shields.io/badge/NLP-Powered-blue", width=120)
    st.markdown("## ⚙️ Settings")
    st.markdown("Adjust analysis parameters below:")
    
    top_n = st.slider(
        "Skills to analyze", 
        min_value=50, max_value=500, 
        value=300, step=50,
        help="More skills = broader analysis but slower"
    )
    top_recs = st.slider(
        "Gap recommendations to show", 
        min_value=5, max_value=20, 
        value=10, step=5
    )
    
    st.markdown("---")
    st.markdown("### 📄 Syllabus")
    st.markdown("Currently loaded: `data/syllabus.txt`")
    st.markdown("*(BSc CS — 6 Semesters)*")
    
    st.markdown("---")
    run_btn = st.button("🚀 Run Analysis", use_container_width=True, type="primary")
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("""
    Built by **Parth Koli**  
    Final Year BSc CS  
    Satish Pradhan Dnyanasadhana College, Thane  
    """)

# Main content
if run_btn:
    with st.spinner("🔍 Analyzing 32,000+ tech job postings... please wait ⏳"):
        df_report, recommendations = run_analysis(
            top_n_skills=top_n,
            top_n_recommendations=top_recs
        )

    gaps = df_report[df_report['is_gap'] == True]
    covered = df_report[df_report['is_gap'] == False]
    coverage_pct = round(len(covered) / len(df_report) * 100, 1)

    # Metrics
    st.markdown("## 📊 Analysis Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🔎 Skills Analyzed", len(df_report))
    col2.metric("✅ Covered in Syllabus", len(covered), delta="Good")
    col3.metric("❌ Skill Gaps Found", len(gaps), delta=f"-{len(gaps)}", delta_color="inverse")
    col4.metric("📈 Coverage", f"{coverage_pct}%")

    st.markdown("---")

    # Progress bar
    st.markdown(f"### Syllabus Coverage: **{coverage_pct}%**")
    st.progress(coverage_pct / 100)
    if coverage_pct < 30:
        st.warning("⚠️ Low coverage — significant gaps found. Focus on self-learning the missing skills!")
    elif coverage_pct < 60:
        st.info("📘 Moderate coverage — some key skills missing. Check recommendations below.")
    else:
        st.success("🎉 Good coverage — your syllabus aligns well with industry!")

    st.markdown("---")

    # Tables
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### ❌ Top Skill Gaps")
        st.caption("High industry demand but missing from syllabus")
        gap_display = gaps[['skill', 'industry_frequency']].head(15).reset_index(drop=True)
        gap_display.index += 1
        gap_display.columns = ['Skill', 'Industry Demand']
        st.dataframe(gap_display, use_container_width=True, height=400)

    with col_right:
        st.markdown("### ✅ Skills Covered")
        st.caption("Already present in your curriculum")
        covered_display = covered[['skill', 'industry_frequency']].head(15).reset_index(drop=True)
        covered_display.index += 1
        covered_display.columns = ['Skill', 'Industry Demand']
        st.dataframe(covered_display, use_container_width=True, height=400)

    st.markdown("---")

    # Bar chart
    st.markdown("### 📈 Top 10 Skill Gaps by Industry Demand")
    chart_data = gaps[['skill', 'industry_frequency']].head(10).set_index('skill')
    chart_data.columns = ['Industry Demand']
    st.bar_chart(chart_data, color="#e53e3e")

    st.markdown("---")

    # Recommendations
    st.markdown("### 🎯 Free Learning Resources for Your Gaps")
    st.caption("Click on each skill to expand free course recommendations")
    
    for i, rec in enumerate(recommendations, 1):
        with st.expander(f"{'❌'} {i}. {rec['skill'].upper()} — Industry Demand: {rec['industry_frequency']:,}"):
            cols = st.columns(len(rec['resources']))
            for j, resource in enumerate(rec['resources']):
                with cols[j]:
                    st.markdown(f"**📚 {resource['title']}**")
                    st.markdown(f"🏫 `{resource['platform']}`")
                    st.link_button("Open Course →", resource['url'])

    st.markdown("---")

    # Download
    st.markdown("### 💾 Download Full Report")
    col_dl1, col_dl2 = st.columns(2)
    with col_dl1:
        csv = df_report.to_csv(index=False)
        st.download_button(
            label="⬇️ Download Gap Report (CSV)",
            data=csv,
            file_name="curriculum_gap_report.csv",
            mime="text/csv",
            use_container_width=True
        )
    with col_dl2:
        gaps_only = gaps[['skill', 'industry_frequency']].to_csv(index=False)
        st.download_button(
            label="⬇️ Download Gaps Only (CSV)",
            data=gaps_only,
            file_name="skill_gaps_only.csv",
            mime="text/csv",
            use_container_width=True
        )

else:
    # Landing page
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("### 📄 Step 1\nLoads your college syllabus from `data/syllabus.txt`")
    with col2:
        st.info("### 💼 Step 2\nAnalyzes 32,000+ real LinkedIn tech job postings")
    with col3:
        st.info("### 📊 Step 3\nGenerates a gap report with free learning resources")

    st.markdown("---")
    st.markdown("### 👈 Click **Run Analysis** in the sidebar to start!")
    
    st.markdown("---")
    st.markdown("### 📌 Sample Gaps This Tool Has Found")
    sample_data = {
        'Skill': ['C++', 'NoSQL', 'TypeScript', 'Jenkins', 'Terraform', 'Tableau', 'JIRA', 'Scala'],
        'Industry Demand': [2748, 1943, 1919, 1861, 1835, 1764, 1704, 1882],
        'Status': ['❌ Gap', '❌ Gap', '❌ Gap', '❌ Gap', '❌ Gap', '❌ Gap', '❌ Gap', '❌ Gap']
    }
    st.dataframe(pd.DataFrame(sample_data), use_container_width=True, hide_index=True)