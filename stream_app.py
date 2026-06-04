import streamlit as st
from PyPDF2 import PdfReader
import re

# Title
st.title("AI Resume Screener")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)

# Job Description
job_description = st.text_area(
    "Paste Job Description Here"
)

analyze = st.button("Analyze Resume")

# Run only after uploading PDF
if uploaded_file is not None and analyze:

    # Read PDF
    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    # Skills List
    skills_list = [
        "Python",
        "Java",
        "JavaScript",
        "HTML",
        "CSS",
        "React",
        "Node",
        "Express",
        "MongoDB",
        "Git",
        "GitHub",
        "SQL",
        "AWS",
        "Data Structures",
        "Operating System"
    ]

    # Resume Skills
    found_skills = []

    for skill in skills_list:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, resume_text, re.IGNORECASE):
            found_skills.append(skill)

    st.subheader("Skills Found")

    for skill in found_skills:
        st.write("✅", skill)

    # JD Skills
    jd_skills = []

    for skill in skills_list:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, job_description, re.IGNORECASE):
            jd_skills.append(skill)

    # Matched Skills
    matched = []

    for skill in jd_skills:
        if skill in found_skills:
            matched.append(skill)

    # ATS Score
    if len(jd_skills) > 0:

        percentage = (len(matched) / len(jd_skills)) * 100

        st.subheader("ATS Score")

        if percentage >= 80:
            st.success(f"ATS Score: {round(percentage,2)} %")

        elif percentage >= 60:
            st.warning(f"ATS Score: {round(percentage,2)} %")

        else:
            st.error(f"ATS Score: {round(percentage,2)} %")

        st.progress(int(percentage))

    # Matched Skills
    st.subheader("Matched Skills")

    for skill in matched:
        st.write("✅", skill)

    # Missing Skills
    missing = []

    for skill in jd_skills:
        if skill not in found_skills:
            missing.append(skill)

    st.subheader("Missing Skills")

    for skill in missing:
        st.write("❌", skill)

    # Recommendations
    recommendations = {
        "SQL": "Learn Joins, Subqueries and GROUP BY",
        "AWS": "Learn EC2, S3 and IAM",
        "MongoDB": "Learn Aggregation Pipeline",
        "Git": "Learn Branching and Merging",
        "Python": "Learn OOP, APIs and Pandas"
    }

    st.subheader("Recommendations")

    for skill in missing:
        if skill in recommendations:
            st.write(f"📌 {skill}: {recommendations[skill]}")

    