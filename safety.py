DANGEROUS_KEYWORDS = [
    "format", "del /f", "shutdown", "taskkill", "erase", "rm", "rmdir", "reg delete"
]

def is_safe_command(command: str) -> bool:
    for word in DANGEROUS_KEYWORDS:
        if word.lower() in command.lower():
            return False
    return True
