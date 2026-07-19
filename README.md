# 📚 Curriculum Gap Analyzer

> An NLP-powered tool that compares college syllabuses against real industry job requirements to identify skill gaps and recommend free learning resources.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![NLP](https://img.shields.io/badge/NLP-spaCy%20%7C%20sklearn-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🎯 Problem Statement

University syllabuses are updated infrequently and often lag behind fast-moving industry demands. Students graduate without knowing exactly which skills they're missing — leading to poor placement outcomes.

**Curriculum Gap Analyzer** solves this by automatically identifying the gaps between what your syllabus teaches and what companies are actually hiring for.

---

## ✨ Features

- 🔍 Analyzes 32,000+ real LinkedIn tech job postings
- 📊 Identifies skill gaps with industry demand frequency
- ✅ Shows which syllabus topics are already industry-aligned
- 🎯 Recommends free learning resources (NPTEL, Coursera, YouTube) for each gap
- 📈 Visual bar charts for gap distribution
- 💾 Export full gap report as CSV
- ⚙️ Adjustable analysis settings via sidebar
- 📄 Upload your own syllabus (TXT or PDF)
- 📝 Upload your resume to personalize gap analysis
- 🎯 Role-specific analysis (Data Scientist, Software Engineer, DevOps, and 14 more)
- 🔐 User login & signup with saved reports history
- 🌐 Live deployed on Streamlit Community Cloud

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| NLP | spaCy, NLTK, scikit-learn (TF-IDF) |
| Data Processing | pandas, NumPy |
| Visualization | Streamlit charts, matplotlib |
| UI | Streamlit |
| Dataset | LinkedIn Job Postings 2024 (Kaggle) |
| Version Control | Git / GitHub |

---

## 📁 Project Structure

```
curriculum-gap-analyzer/
├── app/
│   ├── __init__.py
│   ├── preprocess.py      # Data loading, cleaning, tech job filtering
│   ├── matcher.py         # TF-IDF gap analysis engine
│   ├── recommender.py     # Free resource recommendations
│   └── main.py            # Pipeline orchestrator
├── data/
│   ├── syllabus.txt       # College syllabus input
│   └── gap_report.csv     # Generated gap report (auto-created)
├── streamlit_app.py       # Main Streamlit dashboard
├── requirements.txt       # Python dependencies
├── CHANGELOG.md           # Daily development log
└── README.md
```

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/ParthKoli07/curriculum-gap-analyzer.git
cd curriculum-gap-analyzer
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Download the dataset
Download the LinkedIn Job Postings dataset from Kaggle:
👉 [1.3M LinkedIn Jobs & Skills 2024](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024)

Place these two files in the `data/` folder:
- `job_skills.csv`
- `linkedin_job_postings.csv`

### 5. Run the app
```bash
streamlit run streamlit_app.py
```

---

## 📊 Sample Output

| Metric | Value |
|---|---|
| Total Skills Analyzed | 300 |
| Skills Covered in Syllabus | 71 |
| Skill Gaps Found | 229 |
| Coverage Percentage | 23.7% |

**Top Skill Gaps Identified:**
- C++, NoSQL, TypeScript, Scala, Jenkins, Terraform, Tableau, JIRA

**Top Skills Already Covered:**
- Python, SQL, Java, AWS, Docker, Kubernetes, JavaScript, Agile

---

## 🚀 Live Demo

👉 **[Try it live: curriculum-gap-analyzer.streamlit.app](https://curriculum-gap-analyzer.streamlit.app)**

## 👨‍💻 Author

**Parth Koli**
Final Year BSc Computer Science
Satish Pradhan Dnyanasadhana College, Thane

---

## 📄 License

This project is licensed under the MIT License.