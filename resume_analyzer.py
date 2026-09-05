import re
import json
import nltk
from collections import Counter

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# ---------------------------------------------------------
# NLTK DATA
# ---------------------------------------------------------

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", quiet=True)

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet", quiet=True)


# ---------------------------------------------------------
# RESUME ANALYZER
# ---------------------------------------------------------

class ResumeAnalyzer:

    def __init__(self):

        self.lemmatizer = WordNetLemmatizer()

        self.stop_words = set(
            stopwords.words("english")
        )

        # Load skill database
        with open(
            "skills.json",
            "r",
            encoding="utf-8"
        ) as file:

            self.skills_data = json.load(file)

        self.technical_skills = (
            self.skills_data["technical"]
        )

        self.soft_skills = (
            self.skills_data["soft"]
        )

        self.all_technical_skills = []

        for category, skills in self.technical_skills.items():

            self.all_technical_skills.extend(
                skills
            )


    # -----------------------------------------------------
    # TEXT PREPROCESSING
    # -----------------------------------------------------

    def preprocess_text(self, text):

        text = text.lower()

        text = re.sub(
            r"[^a-zA-Z0-9\s+#.\-]",
            " ",
            text
        )

        tokens = nltk.word_tokenize(
            text
        )

        tokens = [
            self.lemmatizer.lemmatize(token)
            for token in tokens
            if token not in self.stop_words
            and len(token) > 2
        ]

        return " ".join(tokens)


    # -----------------------------------------------------
    # SKILL EXTRACTION
    # -----------------------------------------------------

    def extract_skills(self, text):

        text_lower = text.lower()

        technical = []
        soft = []

        # Technical skills
        for category, skills in self.technical_skills.items():

            for skill in skills:

                pattern = (
                    r"(?<!\w)"
                    + re.escape(skill.lower())
                    + r"(?!\w)"
                )

                if re.search(
                    pattern,
                    text_lower
                ):

                    technical.append(
                        skill
                    )

        # Soft skills
        for skill in self.soft_skills:

            pattern = (
                r"(?<!\w)"
                + re.escape(skill.lower())
                + r"(?!\w)"
            )

            if re.search(
                pattern,
                text_lower
            ):

                soft.append(
                    skill
                )

        technical = list(
            dict.fromkeys(technical)
        )

        soft = list(
            dict.fromkeys(soft)
        )

        return {
            "technical": technical,
            "soft": soft,
            "all": technical + soft,
            "total": len(technical) + len(soft)
        }


    # -----------------------------------------------------
    # EXPERIENCE EXTRACTION
    # -----------------------------------------------------

    def extract_experience(self, text):

        patterns = [

            r"(\d+)\+?\s*years?\s+of\s+experience",

            r"(\d+)\+?\s*years?\s+experience",

            r"(\d+)\+?\s*years?"
        ]

        years = 0

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                years = int(
                    match.group(1)
                )

                break

        experience_keywords = [

            "experience",
            "internship",
            "worked",
            "developed",
            "managed",
            "led",
            "designed",
            "implemented",
            "built",
            "created",
            "deployed",
            "maintained",
            "optimized",
            "analyzed"
        ]

        text_lower = text.lower()

        keyword_count = 0

        detected_keywords = []

        for keyword in experience_keywords:

            if keyword in text_lower:

                keyword_count += 1

                detected_keywords.append(
                    keyword
                )

        has_experience = (
            years > 0
            or keyword_count >= 2
        )

        return {
            "years": years,
            "keyword_score": keyword_count,
            "keywords": detected_keywords,
            "has_experience": has_experience
        }


    # -----------------------------------------------------
    # EDUCATION EXTRACTION
    # -----------------------------------------------------

    def extract_education(self, text):

        education_keywords = [

            "bachelor",
            "master",
            "phd",
            "degree",
            "university",
            "college",
            "school",
            "b.tech",
            "b.e",
            "m.tech",
            "mba",
            "b.sc",
            "m.sc",
            "bca",
            "mca",
            "computer science",
            "engineering"
        ]

        text_lower = text.lower()

        found = []

        for keyword in education_keywords:

            if keyword in text_lower:

                found.append(
                    keyword
                )

        found = list(
            dict.fromkeys(found)
        )

        return {
            "has_education": len(found) > 0,
            "education_keywords": found,
            "score": min(
                len(found),
                5
            )
        }


    # -----------------------------------------------------
    # SECTION DETECTION
    # -----------------------------------------------------

    def detect_sections(self, text):

        sections = {

            "summary": False,

            "education": False,

            "experience": False,

            "skills": False,

            "projects": False,

            "certifications": False,

            "achievements": False,

            "contact": False
        }

        text_lower = text.lower()

        section_variations = {

            "summary": [
                "summary",
                "profile",
                "objective",
                "professional summary"
            ],

            "education": [
                "education",
                "academic",
                "academic background"
            ],

            "experience": [
                "experience",
                "work experience",
                "professional experience",
                "employment"
            ],

            "skills": [
                "skills",
                "technical skills",
                "core skills"
            ],

            "projects": [
                "projects",
                "project",
                "academic projects"
            ],

            "certifications": [
                "certifications",
                "certificates",
                "certification"
            ],

            "achievements": [
                "achievements",
                "accomplishments",
                "awards"
            ],

            "contact": [
                "email",
                "phone",
                "linkedin",
                "github"
            ]
        }

        for section, keywords in section_variations.items():

            for keyword in keywords:

                if keyword in text_lower:

                    sections[section] = True

                    break

        # Contact information
        if re.search(
            r"[\w\.-]+@[\w\.-]+\.\w+",
            text
        ):

            sections["contact"] = True

        return sections


    # -----------------------------------------------------
    # KEYWORD ANALYSIS
    # -----------------------------------------------------

    def keyword_analysis(self, text):

        words = re.findall(
            r"\b[a-zA-Z][a-zA-Z+#.-]{2,}\b",
            text.lower()
        )

        filtered_words = [

            word

            for word in words

            if word not in self.stop_words

            and len(word) > 3
        ]

        frequency = Counter(
            filtered_words
        )

        return dict(
            frequency.most_common(15)
        )


    # -----------------------------------------------------
    # ATS CHECK
    # -----------------------------------------------------

    def ats_check(
        self,
        text,
        sections
    ):

        issues = []

        score = 100

        word_count = len(
            text.split()
        )

        # Length
        if word_count < 150:

            issues.append(
                "Resume contains very little text."
            )

            score -= 15

        elif word_count > 1200:

            issues.append(
                "Resume may be too lengthy."
            )

            score -= 10

        # Email
        email_pattern = (
            r"[\w\.-]+@[\w\.-]+\.\w+"
        )

        if not re.search(
            email_pattern,
            text
        ):

            issues.append(
                "Email address may be missing."
            )

            score -= 10

        # Phone
        phone_pattern = (
            r"(?:\+91[\s-]?)?[6-9]\d{9}"
        )

        if not re.search(
            phone_pattern,
            text
        ):

            issues.append(
                "Phone number may be missing."
            )

            score -= 10

        # Required sections
        required_sections = [

            "experience",
            "education",
            "skills"
        ]

        for section in required_sections:

            if not sections[section]:

                issues.append(
                    f"Missing {section.title()} section."
                )

                score -= 10

        # Projects
        if not sections["projects"]:

            issues.append(
                "Projects section is missing."
            )

            score -= 5

        # Certifications
        if not sections["certifications"]:

            issues.append(
                "Certifications section is missing or not detected."
            )

            score -= 5

        score = max(
            0,
            min(score, 100)
        )

        return {
            "ats_score": score,
            "issues": issues
        }


    # -----------------------------------------------------
    # RESUME SCORE
    # -----------------------------------------------------

    def calculate_score(
        self,
        skills,
        experience,
        education,
        sections,
        text
    ):

        score = 0

        # ---------------------------------------------
        # Technical skills: 30 points
        # ---------------------------------------------

        technical_score = min(
            len(skills["technical"]) * 3,
            30
        )

        score += technical_score

        # ---------------------------------------------
        # Soft skills: 10 points
        # ---------------------------------------------

        soft_score = min(
            len(skills["soft"]) * 2,
            10
        )

        score += soft_score

        # ---------------------------------------------
        # Experience: 20 points
        # ---------------------------------------------

        if experience["has_experience"]:

            experience_score = min(

                experience["years"] * 4
                + experience["keyword_score"],

                20
            )

            score += experience_score

        # ---------------------------------------------
        # Education: 15 points
        # ---------------------------------------------

        if education["has_education"]:

            education_score = min(

                education["score"] * 3,

                15
            )

            score += education_score

        # ---------------------------------------------
        # Projects: 10 points
        # ---------------------------------------------

        if sections["projects"]:

            score += 10

        # ---------------------------------------------
        # Resume sections: 10 points
        # ---------------------------------------------

        section_count = sum(
            sections.values()
        )

        section_score = min(
            section_count * 2,
            10
        )

        score += section_score

        # ---------------------------------------------
        # Content quality: 5 points
        # ---------------------------------------------

        word_count = len(
            text.split()
        )

        if word_count >= 500:

            score += 5

        elif word_count >= 300:

            score += 3

        elif word_count >= 150:

            score += 2

        return min(
            score,
            100
        )


    # -----------------------------------------------------
    # FEEDBACK GENERATION
    # -----------------------------------------------------

    def generate_feedback(
        self,
        skills,
        experience,
        education,
        sections,
        score
    ):

        feedback = []

        # Skills
        if len(
            skills["technical"]
        ) < 3:

            feedback.append(
                "Add more technical skills relevant to your target role."
            )

        elif len(
            skills["technical"]
        ) >= 8:

            feedback.append(
                "Good variety of technical skills has been detected."
            )

        # Soft skills
        if len(
            skills["soft"]
        ) < 2:

            feedback.append(
                "Consider adding relevant soft skills such as communication, teamwork and leadership."
            )

        # Experience
        if not experience["has_experience"]:

            feedback.append(
                "No significant experience was detected. Include internships, projects, freelance work or relevant experience."
            )

        else:

            if experience["years"] < 2:

                feedback.append(
                    "Highlight specific achievements and responsibilities in your experience section."
                )

            feedback.append(
                "Use measurable achievements such as percentages, numbers, users, revenue or performance improvements."
            )

        # Education
        if not education["has_education"]:

            feedback.append(
                "Include your degree, institution and graduation year."
            )

        # Projects
        if not sections["projects"]:

            feedback.append(
                "Add a Projects section containing 2-4 relevant projects."
            )

        # Certifications
        if not sections["certifications"]:

            feedback.append(
                "Consider adding relevant certifications, courses or training."
            )

        # Summary
        if not sections["summary"]:

            feedback.append(
                "Consider adding a concise professional summary tailored to your target role."
            )

        # Achievements
        if not sections["achievements"]:

            feedback.append(
                "Add an Achievements or Awards section if you have relevant accomplishments."
            )

        # Overall score
        if score < 40:

            feedback.append(
                "Your resume needs significant improvement. Focus on adding relevant skills, projects, education and experience."
            )

        elif score < 60:

            feedback.append(
                "Your resume is developing well but needs stronger details and role-specific content."
            )

        elif score < 80:

            feedback.append(
                "Your resume is good. Add more quantifiable achievements and relevant keywords to make it stronger."
            )

        else:

            feedback.append(
                "Excellent resume profile. Continue tailoring your resume for each target position."
            )

        return feedback


    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    def generate_summary(
        self,
        score,
        skills,
        experience,
        education
    ):

        summary = ""

        summary += (
            f"Resume Score: {score}/100\n"
        )

        summary += (
            f"Technical Skills Found: "
            f"{len(skills['technical'])}\n"
        )

        summary += (
            f"Soft Skills Found: "
            f"{len(skills['soft'])}\n"
        )

        summary += (
            f"Experience Years: "
            f"{experience['years']}\n"
        )

        summary += (
            f"Education Detected: "
            f"{'Yes' if education['has_education'] else 'No'}\n"
        )

        summary += (
            f"Experience Detected: "
            f"{'Yes' if experience['has_experience'] else 'No'}\n"
        )

        return summary


    # -----------------------------------------------------
    # COMPLETE ANALYSIS
    # -----------------------------------------------------

    def analyze_resume(self, text):

        skills = self.extract_skills(
            text
        )

        experience = self.extract_experience(
            text
        )

        education = self.extract_education(
            text
        )

        sections = self.detect_sections(
            text
        )

        keywords = self.keyword_analysis(
            text
        )

        score = self.calculate_score(
            skills,
            experience,
            education,
            sections,
            text
        )

        ats = self.ats_check(
            text,
            sections
        )

        feedback = self.generate_feedback(
            skills,
            experience,
            education,
            sections,
            score
        )

        summary = self.generate_summary(
            score,
            skills,
            experience,
            education
        )

        return {

            "skills": skills,

            "experience": experience,

            "education": education,

            "sections": sections,

            "keywords": keywords,

            "score": score,

            "ats": ats,

            "feedback": feedback,

            "summary": summary
        }


    # -----------------------------------------------------
    # TEXT REPORT
    # -----------------------------------------------------

    def generate_text_report(
        self,
        result
    ):

        report = ""

        report += (
            "========================================\n"
        )

        report += (
            "       AI RESUME REVIEWER REPORT\n"
        )

        report += (
            "========================================\n\n"
        )

        report += (
            f"Resume Score: "
            f"{result['score']}/100\n"
        )

        report += (
            f"ATS Score: "
            f"{result['ats']['ats_score']}/100\n\n"
        )

        report += (
            "TECHNICAL SKILLS\n"
        )

        report += (
            ", ".join(
                result["skills"]["technical"]
            )
            or "None detected"
        )

        report += "\n\n"

        report += (
            "SOFT SKILLS\n"
        )

        report += (
            ", ".join(
                result["skills"]["soft"]
            )
            or "None detected"
        )

        report += "\n\n"

        report += (
            "EXPERIENCE\n"
        )

        report += (
            f"Years: "
            f"{result['experience']['years']}\n"
        )

        report += (
            f"Experience detected: "
            f"{result['experience']['has_experience']}\n\n"
        )

        report += (
            "EDUCATION\n"
        )

        report += (
            ", ".join(
                result["education"]["education_keywords"]
            )
            or "None detected"
        )

        report += "\n\n"

        report += (
            "ATS ISSUES\n"
        )

        if result["ats"]["issues"]:

            for issue in result["ats"]["issues"]:

                report += (
                    f"- {issue}\n"
                )

        else:

            report += (
                "No major ATS issues detected.\n"
            )

        report += "\n"

        report += (
            "IMPROVEMENT SUGGESTIONS\n"
        )

        for feedback in result["feedback"]:

            report += (
                f"- {feedback}\n"
            )

        report += "\n"

        report += (
            "========================================\n"
        )

        return report