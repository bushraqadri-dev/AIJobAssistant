import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_ai_suggestions(missing_skills):
    if not missing_skills:
        return "Your resume already covers all detected job skills."

    skills_text = ", ".join(missing_skills)

    prompt = f"""
You are a career assistant.

The candidate is missing these skills for a job:
{skills_text}

Give practical beginner-friendly suggestions for each missing skill.
Keep the response concise and use bullet points.
"""
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text