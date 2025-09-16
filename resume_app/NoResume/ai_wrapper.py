import os
from .models import User, Skill, Experience
from openai import OpenAI

# Load .env file
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def content_generator(user_id):

    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)
    user = User.objects.filter(id=user_id)
    user_skills = Skill.objects.filter(user=user)
    user_experience = Experience.objects.filter(user=user)

    user_data = (
        f"Name: {user.name}\n"
        f"Email: {user.email}\n"
        f"Address: {user.address}\n"
        f"Link: {user.link}\n"
        "Skills:\n"
        + "\n".join(
            f"- {skill.skill_name} ({skill.skill_proficiency}) from {skill.source}"
            for skill in user_skills
        )
        + "\nExperience:\n"
        + "\n".join(
            f"- {exp.experience_name} at {exp.organization} ({exp.start_date} - {exp.end_date})"
            for exp in user_experience
        )
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume writer and career coach. Your task is to generate a professional, accurate, and well-formatted resume based strictly on the information provided. "
                "Do not invent or embellish any details. Ensure all sections are clear, concise, and free of errors. Use standard resume structure and language. "
                "If any required information is missing, leave that section blank or note it as 'Information not provided.'",
            },
            {
                "role": "user",
                "content": f"Generate a resume using the following data:\n{user_data}",
            },
        ],
    )

    return response.choices[0].message.content
