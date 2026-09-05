# 📄 AI Resume Reviewer

An AI-powered resume analysis application built with Python, Natural Language Processing (NLP), text analysis, and rule-based scoring. The application allows users to upload a PDF resume and receive a detailed analysis of their skills, experience, education, resume structure, ATS compatibility, keywords, overall score, and improvement suggestions.

This project was developed for the Data Alcott Systems AI & Data Science Internship task **AI-SS-004: AI Resume Reviewer**. The reference task describes the project as a system that analyzes resumes using NLP and machine learning techniques to provide scoring, feedback, and improvement suggestions. 

---

## 🚀 Project Overview

A resume is one of the most important documents used during internship and job applications. However, many resumes contain missing sections, insufficient skills, weak descriptions, poor keyword usage, or formatting issues that can reduce their effectiveness.

The **AI Resume Reviewer** addresses this problem by automatically analyzing the content of a resume and providing structured feedback.

The system follows this general pipeline:

```text
                📄 Resume PDF
                     │
                     ▼
             📑 PDF Text Extraction
                     │
                     ▼
             🧹 Text Preprocessing
                     │
                     ▼
              🔍 Resume Analysis
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     Skills      Experience    Education
        │            │            │
        └────────────┼────────────┘
                     ▼
              📑 Section Detection
                     │
                     ▼
              🔑 Keyword Analysis
                     │
                     ▼
              📊 Resume Scoring
                     │
                     ▼
              🤖 ATS Compatibility
                     │
                     ▼
              💡 Feedback Generation
                     │
                     ▼
              📊 Results Dashboard
```

The reference task specifically identifies text preprocessing, resume parsing, keyword extraction, resume scoring, feedback generation, and ATS compatibility as important project objectives/features. 

---

# ✨ Features

## 📄 1. PDF Resume Upload

Users can upload their resume directly in PDF format through the Streamlit interface.

The application extracts the textual content from the uploaded PDF and uses it for further analysis.

> Best results are obtained with text-based PDF resumes.

---

## 🧹 2. NLP Text Preprocessing

The application preprocesses resume text by:

* Converting text to lowercase
* Removing unnecessary characters
* Tokenizing text
* Removing stop words
* Performing lemmatization
* Preparing text for analysis

This follows the NLP preprocessing approach described in the reference implementation. 

---

## 🛠️ 3. Technical Skill Extraction

The application identifies technical skills from the resume using a predefined skill database.

Examples include:

### Programming

* Python
* Java
* C
* C++
* JavaScript
* TypeScript
* SQL
* R

### Web Development

* HTML
* CSS
* React
* Angular
* Vue
* Django
* Flask
* FastAPI
* Node.js

### Data Science & AI

* Machine Learning
* Deep Learning
* NLP
* Computer Vision
* TensorFlow
* PyTorch
* Pandas
* NumPy
* Scikit-learn
* OpenCV

### Databases

* MySQL
* PostgreSQL
* MongoDB
* Oracle
* SQLite
* Firebase

### Cloud & DevOps

* AWS
* Azure
* Google Cloud
* Docker
* Kubernetes

### Tools

* Git
* GitHub
* Linux
* Power BI
* Tableau
* Jupyter
* VS Code

The reference task also recommends categorizing technical skills into areas such as programming, web development, data science, databases, and cloud technologies. 

---

# 🤝 4. Soft Skill Detection

The system also identifies soft skills mentioned in the resume.

Examples:

* Communication
* Teamwork
* Leadership
* Problem Solving
* Time Management
* Adaptability
* Creativity
* Critical Thinking
* Collaboration
* Decision Making
* Analytical Thinking
* Presentation

The reference implementation includes communication, teamwork, leadership, problem solving, time management, adaptability, and creativity among its soft-skill categories. 

---

# 💼 5. Experience Analysis

The application analyzes experience-related information.

It attempts to detect:

* Years of experience
* Internship experience
* Work experience
* Experience-related keywords
* Development activities
* Management activities
* Project implementation
* Leadership activities

Experience keywords include terms such as:

```text
developed
managed
led
designed
implemented
built
created
deployed
maintained
optimized
analyzed
```

The reference task similarly uses years of experience and experience-related keywords as part of its analysis. 

---

# 🎓 6. Education Detection

The application searches for education-related information such as:

* Bachelor's degree
* Master's degree
* PhD
* B.Tech
* B.E.
* B.Sc.
* M.Sc.
* BCA
* MCA
* MBA
* University
* College
* Computer Science
* Engineering

It reports whether education information was detected and displays the relevant detected keywords.

Education extraction is one of the core features specified by the reference task. 

---

# 📑 7. Resume Section Detection

The system checks whether important resume sections are present.

Supported sections include:

* Professional Summary
* Education
* Experience
* Skills
* Projects
* Certifications
* Achievements
* Contact Information

The application displays each section as either:

```text
✅ Detected
```

or

```text
❌ Missing
```

This helps users identify incomplete resume structures.

---

# 🔑 8. Keyword Analysis

The application analyzes frequently occurring words in the resume.

It:

1. Extracts words from the resume
2. Removes common stop words
3. Counts word frequency
4. Displays frequently occurring keywords

Example:

```text
Keyword             Occurrences
--------------------------------
python                   8
machine                  5
project                  4
data                     4
developed                3
```

This can help users understand which terms dominate their resume.

---

# 📊 9. Resume Scoring

The application calculates an overall resume score out of **100**.

The scoring model considers:

| Category         | Maximum |
| ---------------- | ------: |
| Technical Skills |      30 |
| Soft Skills      |      10 |
| Experience       |      20 |
| Education        |      15 |
| Projects         |      10 |
| Resume Sections  |      10 |
| Content Quality  |       5 |
| **Total**        | **100** |

The reference project also specifies an overall resume score out of 100 and provides a scoring approach based on skills, experience, education, and resume quality. 

### Example

```text
Resume Score: 82/100
```

The score should be interpreted as an **automated heuristic assessment**, not as an objectively validated measure of resume quality.

---

# 🤖 10. ATS Compatibility Check

The application includes an ATS compatibility checker as an advanced feature.

It checks for common issues such as:

* Missing email address
* Missing phone number
* Missing education section
* Missing experience section
* Missing skills section
* Missing projects section
* Missing certifications section
* Extremely short resume
* Extremely long resume

Example:

```text
ATS Score: 85/100

Potential Issues:

⚠️ Projects section is missing.
⚠️ Certifications section is missing.
```

ATS compatibility checking is explicitly listed as a bonus feature in the reference task. 

---

# 💡 11. Improvement Suggestions

The application generates actionable suggestions based on the analysis.

Examples:

```text
💡 Add more technical skills relevant to your target role.

💡 Consider adding relevant soft skills.

💡 Highlight specific achievements and responsibilities.

💡 Add measurable achievements using numbers or percentages.

💡 Add a Projects section containing 2-4 relevant projects.

💡 Include your degree, institution and graduation year.

💡 Consider adding relevant certifications.
```

The reference specifically requires the system to generate actionable feedback for resume improvement. 

---

# 📥 12. Downloadable Analysis Report

After analysis, users can download a text-based report containing:

* Resume score
* ATS score
* Technical skills
* Soft skills
* Experience information
* Education information
* ATS issues
* Improvement suggestions

Example:

```text
========================================
       AI RESUME REVIEWER REPORT
========================================

Resume Score: 82/100
ATS Score: 90/100

TECHNICAL SKILLS
Python, SQL, Machine Learning, Pandas

SOFT SKILLS
Communication, Teamwork, Leadership

EXPERIENCE
Years: 2
Experience detected: True

EDUCATION
Bachelor, University, Computer Science

ATS ISSUES
- Certifications section is missing.

IMPROVEMENT SUGGESTIONS
- Add measurable achievements.
- Add more role-specific keywords.
```

---

# 🌐 13. Streamlit Web Interface

The application uses Streamlit to provide an interactive web interface.

Users do not need to interact with the Python code directly.

The interface provides:

* Resume upload
* Analysis button
* Resume score
* ATS score
* Skill cards
* Experience analysis
* Education analysis
* Resume section analysis
* Keyword analysis
* Improvement suggestions
* Extracted resume text
* Downloadable report

---

# 🧠 NLP Pipeline

The main NLP pipeline is:

```text
Raw Resume Text
       │
       ▼
Lowercase Conversion
       │
       ▼
Character Cleaning
       │
       ▼
Tokenization
       │
       ▼
Stop Word Removal
       │
       ▼
Lemmatization
       │
       ▼
Processed Text
```

After preprocessing, the system performs:

```text
Processed Resume
       │
       ├── Skill Extraction
       │
       ├── Experience Extraction
       │
       ├── Education Detection
       │
       ├── Section Detection
       │
       ├── Keyword Analysis
       │
       └── ATS Analysis
```

The reference task identifies NLP fundamentals including text preprocessing, tokenization and feature extraction as learning objectives. 

---

# 📂 Project Structure

```text
AI-Resume-Reviewer/
│
├── app.py
│
├── resume_analyzer.py
│
├── pdf_parser.py
│
├── skills.json
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
├── sample_resumes/
│   └── sample_resume.txt
│
└── screenshots/
    ├── dashboard.png
    ├── skills.png
    ├── experience.png
    ├── ats.png
    └── feedback.png
```

---

# 📌 File Description

| File                 | Description                             |
| -------------------- | --------------------------------------- |
| `app.py`             | Streamlit web interface                 |
| `resume_analyzer.py` | Main resume analysis and scoring engine |
| `pdf_parser.py`      | PDF text extraction                     |
| `skills.json`        | Technical and soft skill database       |
| `requirements.txt`   | Python dependencies                     |
| `README.md`          | Project documentation                   |
| `.gitignore`         | Files excluded from Git                 |
| `sample_resumes/`    | Sample resume files                     |
| `screenshots/`       | Project screenshots                     |

---

# ⚙️ Requirements

Make sure you have:

* Python 3.9 or newer
* pip
* VS Code or another Python IDE
* A modern web browser

---

# 🛠️ Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project:

```bash
cd AI-Resume-Reviewer
```

---

## 2. Create Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Download NLTK Resources

Run:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
```

The application also handles missing NLTK resources during initialization.

---

# ▶️ Running the Application

Start Streamlit:

```bash
streamlit run app.py
```

Streamlit will provide a local address in the terminal.

Open the displayed address in your browser.

---

# 📄 How to Use

### Step 1

Open the application.

### Step 2

Click:

```text
Upload your resume
```

### Step 3

Select a PDF resume.

### Step 4

Click:

```text
🔍 Analyze Resume
```

### Step 5

Wait for the analysis to finish.

### Step 6

Review:

* Resume score
* ATS score
* Technical skills
* Soft skills
* Experience
* Education
* Resume sections
* Keywords
* ATS issues
* Improvement suggestions

### Step 7

Download the generated analysis report if required.

---

# 📊 Example Output

```text
AI Resume Reviewer

Resume Score
82/100

ATS Score
90/100

Technical Skills
Python
Machine Learning
SQL
Pandas
NumPy
Django
Git
GitHub

Soft Skills
Communication
Teamwork
Leadership
Problem Solving

Experience
Years Detected: 2
Experience Detected: ✅

Education
Education Detected: ✅

Resume Sections
Summary          ✅
Education        ✅
Experience       ✅
Skills           ✅
Projects         ✅
Certifications   ✅
Achievements     ❌

ATS Compatibility
90/100

Improvement Suggestions

💡 Add an Achievements section.
💡 Add measurable accomplishments.
💡 Tailor keywords to the target role.
```

---

# 🧪 Testing

The application should be tested using multiple resumes.

Recommended test cases:

### Test Case 1: Strong Resume

A resume containing:

* Multiple technical skills
* Soft skills
* Education
* Experience
* Projects
* Certifications
* Contact information

Expected result:

```text
High resume score
High ATS score
Few improvement suggestions
```

---

### Test Case 2: Beginner Resume

A resume containing:

* Education
* Few skills
* No professional experience
* One project

Expected result:

```text
Moderate/low score
Experience-related suggestions
Skill-related suggestions
Project suggestions
```

---

### Test Case 3: Incomplete Resume

A resume missing:

* Education
* Experience
* Skills
* Contact information

Expected result:

```text
Low score
Multiple ATS warnings
Multiple improvement suggestions
```

---

### Test Case 4: Short Resume

Upload a very short resume.

The application should identify the limited amount of content and reduce the ATS compatibility score.

---

# 🔍 Limitations

This project is primarily a **rule-based NLP resume analyzer**.

The current system does not:

* Understand the complete semantic meaning of every sentence
* Guarantee actual ATS compatibility
* Predict whether a recruiter will select a candidate
* Automatically determine whether a skill is genuinely possessed
* Replace professional resume review
* Guarantee job placement

The score is based on predefined rules and should therefore be treated as an automated guideline rather than an authoritative evaluation.

The reference task recommends comparing automated scores with manual reviews and testing the system on diverse resumes when evaluating scoring quality. 

---

# 🔮 Future Enhancements

The project can be expanded significantly.

## 1. 🤖 LLM-Based Feedback

Integrate an LLM to provide more contextual suggestions instead of only keyword-based feedback.

For example:

```text
Current:
"Developed Python application."

Suggested:
"Developed a Python-based automation application that reduced
manual processing time by 35%."
```

---

## 2. 🎯 Job Description Matching

Allow the user to upload or paste a job description.

The application could then compare:

```text
Resume Skills
       +
Job Requirements
       ↓
Skill Match %
```

Example:

```text
Job Match Score: 84%

Matched Skills:
✓ Python
✓ SQL
✓ Machine Learning
✓ Pandas

Missing Skills:
✗ Power BI
✗ AWS
```

---

## 3. 📝 Resume Bullet Improvement

The system could identify weak resume statements and suggest stronger versions.

---

## 4. 📊 Advanced Visualization

Future versions could include:

* Skill distribution charts
* Resume score charts
* ATS score visualization
* Skill gap charts
* Job match charts

The reference also lists visualization dashboards as a bonus feature. 

---

## 5. 🧠 BERT / Transformers

Advanced NLP models such as BERT or transformer-based models could be used for semantic similarity and more sophisticated resume analysis. Transformers/BERT are mentioned as optional advanced technologies in the reference. 

---

## 6. 📄 DOCX Support

Future versions could support:

```text
PDF
DOCX
TXT
```

---

## 7. 🎯 Role-Specific Analysis

The reviewer could provide different recommendations for:

* Data Scientist
* AI/ML Engineer
* Software Developer
* Web Developer
* Data Analyst
* Cloud Engineer
* Cybersecurity Analyst

---

# 🔐 Privacy

The application is designed as a local application and does not require a database.

Resume information is processed by the application during analysis and is not intentionally stored in a database.

The reference task also specifies that a database is not required and recommends Python dictionaries or JSON files for storing analysis data/results. 

Users should still avoid uploading resumes containing information they do not want processed by third-party services when extending the application with external APIs or AI services.

---

# 🧰 Technologies Used

| Technology          | Purpose                                   |
| ------------------- | ----------------------------------------- |
| Python              | Application development                   |
| Streamlit           | Web interface                             |
| NLTK                | NLP preprocessing                         |
| PyPDF2              | PDF text extraction                       |
| Pandas              | Data processing and visualization support |
| Scikit-learn        | Machine learning/text-analysis foundation |
| Regular Expressions | Pattern detection                         |
| JSON                | Skill database                            |
| HTML/CSS            | Streamlit UI customization                |

The reference recommends Python, NLTK/spaCy, Pandas and Scikit-learn as the core technology stack and lists PyPDF2, Transformers and BERT as optional advanced technologies. 

---

# 📸 Screenshots

Add at least 5 screenshots to the `screenshots/` directory.

Recommended screenshots:

### 1. Home Page

```text
screenshots/dashboard.png
```

Show the application before uploading a resume.

### 2. Resume Analysis

```text
screenshots/analysis.png
```

Show the overall resume score.

### 3. Skills

```text
screenshots/skills.png
```

Show technical and soft skills.

### 4. ATS

```text
screenshots/ats.png
```

Show ATS compatibility and detected issues.

### 5. Feedback

```text
screenshots/feedback.png
```

Show improvement suggestions.

The internship task requires **5+ screenshots from different features** as part of the submission materials. 

---

# 🎥 Demo Video

The project demo should demonstrate:

1. Opening the application
2. Uploading a resume
3. Extracting resume text
4. Detecting skills
5. Analyzing experience
6. Detecting education
7. Calculating the resume score
8. Checking ATS compatibility
9. Generating feedback
10. Downloading the analysis report

The reference specifically asks the demo to show skill extraction, scoring/feedback, the NLP pipeline, and resume analysis in action. 

### YouTube

```text
Demo Video:
YOUR_YOUTUBE_LINK
```

---

# 🔗 Project Links

### GitHub Repository

```text
YOUR_GITHUB_REPOSITORY_LINK
```

### Demo Video

```text
YOUR_YOUTUBE_VIDEO_LINK
```

### Blog Post

```text
YOUR_BLOG_POST_LINK
```

---

# 📋 Internship Task Information

```text
Task Name:
AI Resume Reviewer

Task ID:
AI-SS-004

Domain:
Student Support & Internship Management NLP

Technology Stack:
Python
NLP
Text Analysis
Machine Learning

Internship:
AI & Data Science Internship

Company:
Data Alcott Systems
```

The reference identifies the task as **AI-SS-004**, under Student Support & Internship Management NLP, with Python, NLP, Text Analysis and Machine Learning as the technology stack. 

---

# 🎯 Learning Objectives

Through this project, the following concepts are practiced:

* Python programming
* Natural Language Processing
* Text preprocessing
* Tokenization
* Stop-word removal
* Lemmatization
* Keyword extraction
* Pattern matching
* Resume parsing
* Skill extraction
* Experience extraction
* Education detection
* Rule-based scoring
* ATS analysis
* Feedback generation
* JSON-based data management
* Streamlit application development
* PDF processing
* Software testing
* Git and GitHub

The reference specifically identifies NLP fundamentals, resume parsing, keyword extraction, resume scoring, feedback generation and ATS compatibility as learning objectives. 

---

# 📈 Project Workflow

```text
                    START
                      │
                      ▼
              Upload Resume PDF
                      │
                      ▼
               Extract PDF Text
                      │
                      ▼
              Clean Resume Text
                      │
                      ▼
                Tokenization
                      │
                      ▼
              Stop Word Removal
                      │
                      ▼
                 Lemmatization
                      │
                      ▼
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       Extract Skills    Analyze Experience
             │                 │
             └────────┬────────┘
                      │
                      ▼
                Detect Education
                      │
                      ▼
               Detect Sections
                      │
                      ▼
               Analyze Keywords
                      │
                      ▼
              Calculate Score
                      │
                      ▼
              ATS Compatibility
                      │
                      ▼
             Generate Feedback
                      │
                      ▼
               Display Results
                      │
                      ▼
              Download Report
                      │
                      ▼
                     END
```

---

# 📝 Submission Checklist

Before submitting the project, make sure everything below is completed:

```text
☐ Resume analysis engine completed
☐ PDF text extraction working
☐ Technical skill extraction working
☐ Soft skill extraction working
☐ Experience extraction working
☐ Education extraction working
☐ Resume scoring algorithm working
☐ Feedback generation working
☐ ATS compatibility implemented
☐ Keyword analysis implemented
☐ Streamlit interface working
☐ Code cleaned and documented
☐ GitHub repository created
☐ README.md included
☐ 5+ screenshots captured
☐ Project report prepared
☐ Demo video recorded
☐ YouTube link active
☐ Blog post prepared
☐ GitHub link added to submission
☐ YouTube link added to submission
```

The official task checklist includes the analysis engine, skill/experience/education extraction, scoring, feedback, clean code, GitHub repository, README, screenshots, report, demo video, YouTube link and blog submission. 

---

# 📅 Suggested 7-Day Development Plan

The reference provides a seven-day development plan. 

| Day   | Task                                        |
| ----- | ------------------------------------------- |
| Day 1 | Research, planning and environment setup    |
| Day 2 | NLP preprocessing and section detection     |
| Day 3 | Technical and soft skill extraction         |
| Day 4 | Experience and education analysis           |
| Day 5 | Scoring and feedback                        |
| Day 6 | ATS, visualization and testing              |
| Day 7 | Documentation, screenshots, report and demo |

---

# 👨‍💻 Author

**Your Name**

AI & Data Science Intern

---

# 📜 License

This project was developed for educational and internship purposes.

---

# ⭐ Acknowledgement

This project was developed as part of the **Data Alcott Systems AI & Data Science Internship**, based on the **AI Resume Reviewer (AI-SS-004)** project requirements.

The project focuses on applying NLP and text-analysis techniques to resume data and generating automated scoring and actionable improvement suggestions. The reference emphasizes that a working resume reviewer with intelligent scoring is more important than having a large dataset. 

---

## ⭐ Project Highlights

```text
📄 PDF Resume Parsing
🧠 NLP Text Processing
🛠️ Skill Extraction
💼 Experience Analysis
🎓 Education Detection
📑 Section Detection
🔑 Keyword Analysis
📊 Resume Scoring
🤖 ATS Compatibility
💡 Intelligent Feedback
📥 Downloadable Report
🌐 Streamlit Web Application
```

**AI Resume Reviewer turns an ordinary resume into a structured, measurable analysis that helps users identify strengths, weaknesses, missing information, and areas for improvement.**