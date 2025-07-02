from llm import get_command_from_prompt
from executor import execute_command
from safety import is_safe_command

def main():
    print("🤖 Welcome to your AI Windows Assistant!")
    while True:
        user_input = input("\n🧠 What do you want to do? (or 'exit') → ")
        if user_input.lower() in ['exit', 'quit']:
            break

        command = get_command_from_prompt(user_input)
        print(f"\n💡 Suggested Command:\n{command}")

        if not is_safe_command(command):
            print("❌ This command might be dangerous. Aborting.")
            continue

        confirm = input("\nRun this command? (y/n): ").lower()
        if confirm == 'y':
            execute_command(command)
        else:
            print("⚠️ Cancelled.")

if __name__ == "__main__":
    main()
