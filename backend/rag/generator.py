import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_answer(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "user", "content": prompt}
        ],
        max_tokens = 300,
    )
    return response.choices[0].message.content

