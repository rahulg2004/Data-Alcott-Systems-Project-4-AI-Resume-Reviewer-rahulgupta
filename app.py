import streamlit as st
import pandas as pd

from pdf_parser import extract_text_from_pdf
from resume_analyzer import ResumeAnalyzer


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }

    .score-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #ddd;
    }

    .score-number {
        font-size: 48px;
        font-weight: 700;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 20px;
    }

    .skill {
        display: inline-block;
        padding: 7px 12px;
        margin: 4px;
        border-radius: 15px;
        background-color: #f0f2f6;
        color: #000000 !important;
        font-size: 14px;
        font-weight: 600;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">📄 AI Resume Reviewer</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Upload your resume and receive an automated analysis,
    resume score, ATS compatibility check and improvement suggestions.
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Resume Reviewer")

    st.write(
        """
        This application analyzes resumes using:

        • NLP  
        • Text Analysis  
        • Skill Extraction  
        • Experience Analysis  
        • Education Detection  
        • Resume Scoring  
        • ATS Compatibility  
        • Feedback Generation
        """
    )

    st.divider()

    st.info(
        "Upload a text-based PDF resume for best results."
    )


# ---------------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload your resume",
    type=["pdf"],
    help="Upload a PDF resume for analysis."
)


# ---------------------------------------------------------
# ANALYSIS
# ---------------------------------------------------------

if uploaded_file is not None:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    analyze_button = st.button(
        "🔍 Analyze Resume",
        use_container_width=True
    )

    if analyze_button:

        with st.spinner(
            "Analyzing your resume..."
        ):

            try:

                # Extract text
                resume_text = extract_text_from_pdf(
                    uploaded_file
                )

                if not resume_text.strip():

                    st.error(
                        "Could not extract text from this PDF. "
                        "Please upload a text-based PDF."
                    )

                    st.stop()

                # Create analyzer
                analyzer = ResumeAnalyzer()

                # Analyze
                result = analyzer.analyze_resume(
                    resume_text
                )

                # Save results in session state
                st.session_state["result"] = result
                st.session_state["resume_text"] = resume_text

            except Exception as error:

                st.error(
                    f"An error occurred: {error}"
                )


# ---------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    st.divider()

    # -----------------------------------------------------
    # SCORE SECTION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">📊 Resume Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Resume Score",
            f"{result['score']}/100"
        )

    with col2:

        st.metric(
            "ATS Score",
            f"{result['ats']['ats_score']}/100"
        )

    with col3:

        st.metric(
            "Technical Skills",
            len(result["skills"]["technical"])
        )

    with col4:

        st.metric(
            "Soft Skills",
            len(result["skills"]["soft"])
        )


    # -----------------------------------------------------
    # SCORE PROGRESS
    # -----------------------------------------------------

    st.subheader("Resume Quality Score")

    st.progress(
        result["score"] / 100
    )


    # -----------------------------------------------------
    # SKILLS
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">🛠️ Skills Detected</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Technical Skills")

        technical_skills = result["skills"]["technical"]

        if technical_skills:

            for skill in technical_skills:

                st.markdown(
                    f'<span class="skill">💻 {skill.title()}</span>',
                    unsafe_allow_html=True
                )

        else:

            st.warning(
                "No technical skills detected."
            )

    with col2:

        st.subheader("Soft Skills")

        soft_skills = result["skills"]["soft"]

        if soft_skills:

            for skill in soft_skills:

                st.markdown(
                    f'<span class="skill">🤝 {skill.title()}</span>',
                    unsafe_allow_html=True
                )

        else:

            st.warning(
                "No soft skills detected."
            )


    # -----------------------------------------------------
    # EXPERIENCE
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">💼 Experience Analysis</div>',
        unsafe_allow_html=True
    )

    experience = result["experience"]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Years Detected",
            experience["years"]
        )

    with col2:

        st.metric(
            "Experience Keywords",
            experience["keyword_score"]
        )

    with col3:

        if experience["has_experience"]:

            st.success(
                "Experience Detected"
            )

        else:

            st.warning(
                "Experience Not Detected"
            )


    # -----------------------------------------------------
    # EDUCATION
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">🎓 Education Analysis</div>',
        unsafe_allow_html=True
    )

    education = result["education"]

    if education["has_education"]:

        st.success(
            "Education information detected."
        )

        if education["education_keywords"]:

            st.write(
                "Detected keywords:"
            )

            st.write(
                ", ".join(
                    education["education_keywords"]
                )
            )

    else:

        st.warning(
            "Education information was not detected."
        )


    # -----------------------------------------------------
    # SECTIONS
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">📑 Resume Sections</div>',
        unsafe_allow_html=True
    )

    sections = result["sections"]

    section_data = []

    for section, detected in sections.items():

        section_data.append(
            {
                "Section": section.title(),
                "Status": "✅ Detected"
                if detected
                else "❌ Missing"
            }
        )

    section_df = pd.DataFrame(
        section_data
    )

    st.dataframe(
        section_df,
        use_container_width=True,
        hide_index=True
    )


    # -----------------------------------------------------
    # ATS CHECK
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">🤖 ATS Compatibility</div>',
        unsafe_allow_html=True
    )

    ats = result["ats"]

    st.progress(
        ats["ats_score"] / 100
    )

    st.write(
        f"**ATS Compatibility Score: "
        f"{ats['ats_score']}/100**"
    )

    if ats["issues"]:

        st.subheader(
            "Potential ATS Issues"
        )

        for issue in ats["issues"]:

            st.warning(
                f"⚠️ {issue}"
            )

    else:

        st.success(
            "No major ATS issues detected."
        )


    # -----------------------------------------------------
    # KEYWORD ANALYSIS
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">🔑 Keyword Analysis</div>',
        unsafe_allow_html=True
    )

    keywords = result["keywords"]

    if keywords:

        keyword_data = []

        for keyword, count in keywords.items():

            keyword_data.append(
                {
                    "Keyword": keyword,
                    "Occurrences": count
                }
            )

        keyword_df = pd.DataFrame(
            keyword_data
        )

        st.dataframe(
            keyword_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No significant keywords detected."
        )


    # -----------------------------------------------------
    # FEEDBACK
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">💡 Improvement Suggestions</div>',
        unsafe_allow_html=True
    )

    feedback = result["feedback"]

    if feedback:

        for item in feedback:

            st.info(
                f"💡 {item}"
            )

    else:

        st.success(
            "No major improvement suggestions."
        )


    # -----------------------------------------------------
    # RESUME SUMMARY
    # -----------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">📝 Analysis Summary</div>',
        unsafe_allow_html=True
    )

    st.text(
        result["summary"]
    )


    # -----------------------------------------------------
    # RAW TEXT
    # -----------------------------------------------------

    with st.expander(
        "📄 View Extracted Resume Text"
    ):

        st.text(
            st.session_state["resume_text"]
        )


    # -----------------------------------------------------
    # DOWNLOAD REPORT
    # -----------------------------------------------------

    report = analyzer.generate_text_report(
        result
    )

    st.download_button(
        label="📥 Download Analysis Report",
        data=report,
        file_name="resume_analysis_report.txt",
        mime="text/plain",
        use_container_width=True
    )


else:

    st.info(
        "👆 Upload a PDF resume above to begin the analysis."
    )