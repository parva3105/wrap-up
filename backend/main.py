from llm import get_command
from executor import execute_command
from safety import is_safe

def main():
    print("🤖 Welcome to your AI Windows Assistant CLI tester!")
    while True:
        prompt = input("\n💬 What do you want to do? (or 'exit') → ")
        if prompt.lower() in ('exit', 'quit'):
            break

        command = get_command(prompt)
        print(f"\n💡 Suggested Command:\n{command}")

        if not is_safe(command):
            print("❌ Unsafe command detected. Aborting.")
            continue

        confirm = input("Run it? (y/n) → ").lower()
        if confirm == 'y':
            result = execute_command(command)
            print("\n🔸 STDOUT:\n", result['stdout'])
            if result['stderr']:
                print("\n⚠️ STDERR:\n", result['stderr'])
        else:
            print("⚠️ Cancelled.")

if __name__ == "__main__":
    main()
