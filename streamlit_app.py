import streamlit as st
import pandas as pd
from app.main import run_analysis
from app.auth import init_db, signup_user, login_user, save_report, get_user_reports

# Initialize database
init_db()

st.set_page_config(
    page_title="Curriculum Gap Analyzer",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .title-text {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
    }
    .subtitle-text {
        font-size: 1.1rem;
        color: #a0aec0;
    }
    .login-box {
        background-color: #1e1e2e;
        padding: 2rem;
        border-radius: 12px;
        max-width: 400px;
        margin: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Session state init
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = "login"

# ─── LOGIN / SIGNUP PAGE ───────────────────────────────────────
def show_auth_page():
    st.markdown('<p class="title-text">📚 Curriculum Gap Analyzer</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Find the gap between your syllabus and industry requirements</p>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign Up"])

        with tab1:
            st.markdown("### Welcome back!")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password", type="password", key="login_password")

            if st.button("Login", use_container_width=True, type="primary"):
                if username and password:
                    success, result = login_user(username, password)
                    if success:
                        st.session_state.logged_in = True
                        st.session_state.user = result
                        st.success(f"Welcome back, {result['username']}! 🎉")
                        st.rerun()
                    else:
                        st.error(result)
                else:
                    st.warning("Please fill in all fields!")

        with tab2:
            st.markdown("### Create an account")
            new_username = st.text_input("Username", key="signup_username")
            new_email = st.text_input("Email", key="signup_email")
            new_college = st.text_input("College Name", key="signup_college", 
                                         placeholder="e.g. Satish Pradhan Dnyanasadhana College")
            new_password = st.text_input("Password", type="password", key="signup_password")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

            if st.button("Sign Up", use_container_width=True, type="primary"):
                if all([new_username, new_email, new_password, confirm_password]):
                    if new_password != confirm_password:
                        st.error("Passwords don't match!")
                    elif len(new_password) < 6:
                        st.error("Password must be at least 6 characters!")
                    else:
                        success, msg = signup_user(new_username, new_email, new_password, new_college)
                        if success:
                            st.success(msg + " Please login.")
                        else:
                            st.error(msg)
                else:
                    st.warning("Please fill in all fields!")

# ─── MAIN APP PAGE ─────────────────────────────────────────────
def show_main_app():
    # Sidebar
    with st.sidebar:
        st.image("https://img.shields.io/badge/NLP-Powered-blue", width=120)
        st.markdown(f"## 👋 Hello, {st.session_state.user['username']}!")
        if st.session_state.user.get('college'):
            st.markdown(f"🏫 *{st.session_state.user['college']}*")
        st.markdown("---")

        st.markdown("## ⚙️ Settings")
        top_n = st.slider("Skills to analyze", min_value=50, max_value=500, value=300, step=50)
        top_recs = st.slider("Gap recommendations to show", min_value=5, max_value=20, value=10, step=5)

        st.markdown("---")
        st.markdown("### 📄 Syllabus")
        syllabus_option = st.radio(
            "Choose syllabus source:",
            ["Use default (BSc CS)", "Upload my own"]
        )

        uploaded_syllabus = None
        if syllabus_option == "Upload my own":
            uploaded_syllabus = st.file_uploader(
                "Upload your syllabus",
                type=["txt", "pdf"],
                help="Upload a .txt or .pdf file of your syllabus"
            )
            if uploaded_syllabus is None:
                st.warning("⚠️ Please upload a syllabus file")

        st.markdown("---")
        st.markdown("### 📄 Resume (Optional)")
        st.markdown("*Upload your resume to personalize the gap analysis*")
        uploaded_resume = st.file_uploader(
            "Upload your resume",
            type=["txt", "pdf"],
            help="Skills found in your resume won't show as gaps"
        )
        if uploaded_resume:
            st.success("✅ Resume uploaded!")


        st.markdown("---")
        run_btn = st.button("🚀 Run Analysis", width='stretch', type="primary")

        st.markdown("---")
        if st.button("🚪 Logout", width='stretch'):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()

        st.markdown("---")
        st.markdown("### ℹ️ About")
        st.markdown("Built by **Parth Koli**  \nFinal Year BSc CS  \nSatish Pradhan Dnyanasadhana College, Thane")

    # Main content
    st.markdown('<p class="title-text">📚 Curriculum Gap Analyzer</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle-text">Compares your college syllabus against real industry job requirements to find skill gaps</p>', unsafe_allow_html=True)
    st.markdown("---")

    # Saved reports section
    reports = get_user_reports(st.session_state.user['id'])
    if reports:
        with st.expander(f"📂 Your Saved Reports ({len(reports)})"):
            for r in reports:
                st.markdown(f"**{r[0]}** — Coverage: {r[1]}% | Gaps: {r[2]} | Covered: {r[3]} | *{r[4]}*")

    if run_btn:
        # Handle syllabus FIRST
        syllabus_text = None
        if syllabus_option == "Upload my own":
            if uploaded_syllabus is None:
                st.error("❌ Please upload a syllabus file first!")
                st.stop()
            if uploaded_syllabus.type == "text/plain":
                syllabus_text = uploaded_syllabus.read().decode("utf-8")
            elif uploaded_syllabus.type == "application/pdf":
                import PyPDF2
                pdf_reader = PyPDF2.PdfReader(uploaded_syllabus)
                syllabus_text = ""
                for page in pdf_reader.pages:
                    syllabus_text += page.extract_text()
        else:
            # Load default syllabus
            from app.preprocess import load_syllabus
            syllabus_text = load_syllabus()

        # Handle resume
        resume_skills = []
        if uploaded_resume is not None:
            from app.resume_parser import extract_skills_from_resume, combine_syllabus_and_resume
            resume_skills = extract_skills_from_resume(uploaded_resume, uploaded_resume.type)
            if resume_skills:
                st.info(f"📄 Found **{len(resume_skills)}** skills in your resume: {', '.join(resume_skills[:10])}{'...' if len(resume_skills) > 10 else ''}")
            syllabus_text = combine_syllabus_and_resume(syllabus_text, resume_skills)

        with st.spinner("🔍 Analyzing 32,000+ tech job postings... please wait ⏳"):
            df_report, recommendations = run_analysis(
                top_n_skills=top_n,
                top_n_recommendations=top_recs,
                syllabus_text=syllabus_text
            )

        if df_report is None:
            st.error("❌ Something went wrong. Please try again.")
            st.stop()

        gaps = df_report[df_report['is_gap'] == True]
        covered = df_report[df_report['is_gap'] == False]
        coverage_pct = round(len(covered) / len(df_report) * 100, 1)

        # Save report automatically
        save_report(
            st.session_state.user['id'],
            f"Analysis #{len(reports)+1}",
            coverage_pct,
            len(gaps),
            len(covered)
        )

        # Metrics
        st.markdown("## 📊 Analysis Summary")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("🔎 Skills Analyzed", len(df_report))
        col2.metric("✅ Covered in Syllabus", len(covered), delta="Good")
        col3.metric("❌ Skill Gaps Found", len(gaps), delta=f"-{len(gaps)}", delta_color="inverse")
        col4.metric("📈 Coverage", f"{coverage_pct}%")

        st.markdown("---")
        st.markdown(f"### Syllabus Coverage: **{coverage_pct}%**")
        st.progress(coverage_pct / 100)
        if coverage_pct < 30:
            st.warning("⚠️ Low coverage — significant gaps found. Focus on self-learning the missing skills!")
        elif coverage_pct < 60:
            st.info("📘 Moderate coverage — some key skills missing. Check recommendations below.")
        else:
            st.success("🎉 Good coverage — your syllabus aligns well with industry!")

        st.markdown("---")

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
        st.markdown("### 📈 Top 10 Skill Gaps by Industry Demand")
        chart_data = gaps[['skill', 'industry_frequency']].head(10).set_index('skill')
        chart_data.columns = ['Industry Demand']
        st.bar_chart(chart_data, color="#e53e3e")

        st.markdown("---")
        st.markdown("### 🎯 Free Learning Resources for Your Gaps")
        st.caption("Click on each skill to expand free course recommendations")
        for i, rec in enumerate(recommendations, 1):
            with st.expander(f"❌ {i}. {rec['skill'].upper()} — Industry Demand: {rec['industry_frequency']:,}"):
                cols = st.columns(len(rec['resources']))
                for j, resource in enumerate(rec['resources']):
                    with cols[j]:
                        st.markdown(f"**📚 {resource['title']}**")
                        st.markdown(f"🏫 `{resource['platform']}`")
                        st.link_button("Open Course →", resource['url'])

        st.markdown("---")
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

# ─── ROUTER ────────────────────────────────────────────────────
if st.session_state.logged_in:
    show_main_app()
else:
    show_auth_page()