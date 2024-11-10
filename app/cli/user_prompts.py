from app.services.user_service import new_user, delete_user, update_user, list_users

class UserPrompts:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("\n=== USER MENU ===")
            print("1. Add User")
            print("2. Delete User")
            print("3. List Users")
            print("4. Update User")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add()
            elif choice == '2':
                self.delete()
            elif choice == '3':
                self.get_users()
            elif choice == '4':
                self.update()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

    def add(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        new_user(name, email)

    def delete(self):
        user_id = input("Enter user id: ")
        delete_user(user_id)

    def update(self):
        user_id = input("Enter user id: ")
        name = input("Enter new name: ")
        email = input("Enter new email: ")
        update_user(user_id, name, email)

    def get_users(self):
        list_users()