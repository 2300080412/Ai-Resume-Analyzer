from pypdf import PdfReader

# Read Resume PDF
reader = PdfReader("resume_1.pdf")

resume_text = ""

for page in reader.pages:
    resume_text += page.extract_text()

# Skills Database
skills_list = [
    "Python",
    "Java",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Node",
    "Express",
    "MongoDB",
    "Git",
    "GitHub",
    "SQL",
    "AWS",
    "Machine Learning",
    "Data Structures",
    "Operating System"
]

# Extract Skills from Resume
found_skills = []

for skill in skills_list:
    if skill.lower() in resume_text.lower():
        found_skills.append(skill)

print("\nResume Skills Found:")
print(found_skills)

# Job Description
job_description = """
We are looking for a Python Developer with experience in
Python, SQL, AWS, MongoDB, Git and JavaScript.
"""

# Extract Skills from JD
jd_skills = []

for skill in skills_list:
    if skill.lower() in job_description.lower():
        jd_skills.append(skill)

print("\nJD Skills:")
print(jd_skills)

# Match Skills
matched = []

for skill in jd_skills:
    if skill in found_skills:
        matched.append(skill)

print("\nMatched Skills:")
print(matched)

# ATS Score
matched_count = len(matched)
total_required = len(jd_skills)

percentage = (matched_count / total_required) * 100

print("\nATS Score:", round(percentage, 2), "%")

# Skill Gap Analysis

missing_skills = []

for skill in jd_skills:
    if skill not in found_skills:
        missing_skills.append(skill)

print("\nMissing Skills:")
print(missing_skills)


recommendations = {
    "SQL": "Learn Joins, Subqueries, Group By",
    "AWS": "Learn EC2, S3, IAM",
    "MongoDB": "Learn Aggregation and Indexing",
    "Python": "Learn OOP, APIs and File Handling"
}

print("\nRecommendations:")

for skill in missing_skills:
    if skill in recommendations:
        print(skill, "->", recommendations[skill])
        
        


'''start = resume_text.find("Projects")
end = resume_text.find("Technical Skills")

print("Start:", start)
print("End:", end)

projects = resume_text[start:end]

print(projects)'''



