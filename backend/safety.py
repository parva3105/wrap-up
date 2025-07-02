DANGEROUS_KEYWORDS = [
    "format", "shutdown", "erase", "reg delete", "del /f", "rmdir", "taskkill", "rm -rf"
]

def is_safe(command: str) -> bool:
    command = command.lower()
    return not any(danger in command for danger in DANGEROUS_KEYWORDS)
