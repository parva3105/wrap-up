from fastapi import FastAPI
from pydantic import BaseModel
from .llm import get_command
from .executor import execute_command
from .safety import is_safe

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

class CommandInput(BaseModel):
    command: str

@app.post("/generate-command")
def generate_command(data: PromptInput):
    command = get_command(data.prompt)
    return {"command" : command}


@app.post("/execute")
def execute_command_api(data: CommandInput):
    if not is_safe(data.command):
        return {"success": False, "error" : "Unsafe Command Detected!"}
    result = execute_command(data.command)
    return result