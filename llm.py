import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a Windows system assistant. Your job is to convert natural language instructions into Windows terminal commands.
Use winget if possible. NEVER use Linux commands like apt, yum, or bash.

Respond with ONLY the command that should be run.
"""

def get_command_from_prompt(prompt: str) -> str:
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
