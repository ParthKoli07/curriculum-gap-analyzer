# Changelog

## [Day 1] — 2026-07-07
### Setup
- Created GitHub repo (curriculum-gap-analyzer)
- Cloned repo locally, opened in VS Code
- Created virtual environment (venv)
- Installed dependencies: pandas, numpy, scikit-learn, spaCy, NLTK, streamlit, PyPDF2, matplotlib, seaborn
- Created folder structure: app/, data/, notebooks/, docs/
- Initialized core module files: preprocess.py, matcher.py, recommender.py, main.py

## [Day 2] — 2026-07-08
### Data & Preprocessing
- Downloaded LinkedIn Job Postings + Skills dataset (1.29M records)
- Built preprocess.py with:
  - load_job_data(): merges job_skills.csv + linkedin_job_postings.csv on job_link
  - clean_text(): normalizes and cleans text
  - extract_skills_list(): extracts top skills with frequency count
  - load_syllabus(): reads syllabus text file
- Successfully tested: 1,296,381 records loaded, top 20 skills extracted
- Removed large CSV files from git tracking, updated .gitignore
- Fixed git history using git-filter-repo to remove large files

## [Day 3] — 2026-07-09
### Core Gap Analysis Engine
- Built matcher.py with:
  - get_industry_skills(): extracts top 300 technical skills, filters soft skills
  - compute_gap(): direct keyword matching between industry skills and syllabus
  - print_gap_summary(): clean report showing gaps vs covered skills
- Created data/syllabus.txt with full 6-semester CS curriculum
- Gap analysis working: 300 skills analyzed, Python/SQL/Java/AWS detected as covered
- Gap report saved to data/gap_report.csv
- Built recommender.py with resource map for 25+ tech skills
- Fixed job filter to CS-specific roles only (32K tech jobs)
- Clean gap results: C++, NoSQL, TypeScript, Terraform, Jenkins, Tableau, JIRA identified as gaps

## [Day 4] — 2026-07-10
### Streamlit UI Dashboard
- Built streamlit_app.py with full interactive dashboard
- Features: analysis summary metrics, skill gap table, covered skills table
- Added bar chart visualization of top 10 skill gaps
- Added expandable free learning resource cards per gap
- Added CSV download button for full gap report
- Full pipeline working end to end via UI

## [Day 5] — 2026-07-11
### UI Polish & Documentation
- Polished Streamlit UI with custom CSS, progress bar, coverage indicator
- Added NLP Powered badge, About section with college info
- Added Step 1/2/3 landing page cards
- Added sample gaps preview table on landing page
- Added two download buttons (full report + gaps only)
- Updated README with full setup instructions, features, tech stack
- Added demo screenshot to docs

## [Day 6] — 2026-07-13
### Resource Improvements & UI Polish
- Added specific course links for 15+ new skills in recommender.py
- Jenkins, Terraform, JIRA, TypeScript, Scala, NoSQL, Kafka, Spark, Redis, Ansible, Golang, Rust, Microservices, CI/CD all now have direct course links
- Verified all links open correctly
- Added noise filters for non-CS skills in matcher.py