import ollama

SYSTEM_PROMPT = """
You are a Windows assistant. Convert natural language into commands that work in Command Prompt (cmd.exe), not PowerShell.

Avoid advanced PowerShell-only commands unless necessary. Prefer things like:
- ipconfig
- winget
- dir
- del

Return only the actual command.
"""

def get_command(prompt: str) -> str:
    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content'].strip()
