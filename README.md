# AI Job Application Assistant

An AI-powered job application assistant that analyzes a resume against a job description and identifies matching and missing skills.

## Features

- Upload a resume in PDF format
- Paste a job description
- Extract text from the resume
- Detect required skills from the job description
- Identify matched skills
- Identify missing skills
- Calculate an overall resume match percentage

## Tech Stack

- Python
- Streamlit
- PyPDF2
- Pandas
- NLP / Text Processing
## How It Works

1. Upload your resume as a PDF.
2. Paste the job description.
3. Click **Analyze Job Match**.
4. The application compares the resume with the job requirements.
5. The application displays matched skills, missing skills, and the overall match percentage.

## Project Structure

```text
AIJobAssistant/
├── app.py
├── resume_parser.py
├── job_matcher.py
├── requirements.txt
└── README.md