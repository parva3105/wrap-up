import subprocess

def execute_command(command: str) -> dict:
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "success": result.returncode == 0
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "success": False
        }
