def match_job(resume_text, job_description):
    skills = [
         "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "postgresql",
    "oracle",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "php",
    "git",
    "github",
    "power bi",
    "tableau",
    "excel",
    "pandas",
    "numpy",
    "machine learning",
    "data analysis",
    "data analytics",
    "testing",
    "selenium",
    "debugging",
    "api",
    "rest api",
    "networking",
    "linux",
    "windows",
    "cloud",
    "aws",
    "azure"
    ]

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    required_skills = [
        skill for skill in skills
        if skill in job_description
    ]

    matched_skills = [
        skill for skill in required_skills
        if skill in resume_text
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_text
    ]

    if required_skills:
        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100
    else:
        match_percentage = 0

    return match_percentage, required_skills, matched_skills, missing_skills
   