import os
from openai import OpenAI

# Load .env file
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


def content_generator(user_message):

    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o",
        # messages=[{"role" : "system", "content":"You are an expert latex content generator and editor."},
        #           {"role":"user","content":""}],
        messages=[
            {
                "role": "system",
                "content": "You are a test platform, generate a message that validates that you are functioning",
            },
            {"role": "user", "content": user_message},
        ],
    )

    return response.choices[0].message.content
