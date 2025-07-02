import subprocess

def execute_command(command: str):
    try:
        print("\n🛠️ Running command...\n")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("📤 Output:\n", result.stdout)
        if result.stderr:
            print("⚠️ Errors:\n", result.stderr)
    except Exception as e:
        print("❌ Failed to execute:", str(e))
