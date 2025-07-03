from fastapi import FastAPI
from pydantic import BaseModel
from llm import get_command
from executor import execute_command
from safety import is_safe
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server origin
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


def run_command(command: str):
    powershell_command = f'powershell -Command "{command}"'
    result = subprocess.run(
        powershell_command,
        shell=True,
        capture_output=True,
        text=True
    )
    return result

class PromptInput(BaseModel):
    prompt: str

class CommandInput(BaseModel):
    command: str

@app.post("/generate-command")
def generate_command(data: PromptInput):
    command = get_command(data.prompt)
    return {"command" : command}


@app.post("/execute")
async def execute_command(data: CommandInput):
    try:
        result = run_command(data.command)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "returncode": -1
        }