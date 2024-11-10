from app.cli.user_prompts import UserPrompts
from app.cli.role_prompts import RolePrompts

def main_menu():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. USER MENU")
        print("2. ROLE MENU")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            UserPrompts()
        elif choice == '2':
            RolePrompts()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()