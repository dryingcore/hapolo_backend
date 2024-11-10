from app.services.role_service import new_role, delete_role, update_role, list_roles

class RolePrompts:
    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("\n=== Role MENU ===")
            print("1. Add Role")
            print("2. Delete Role")
            print("3. List Roles")
            print("4. Update Role")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add()
            elif choice == '2':
                self.delete()
            elif choice == '3':
                self.get_roles()
            elif choice == '4':
                self.update()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

    def add(self):
        name = input("Enter role name: ")
        new_role(name)

    def delete(self):
        user_id = input("Enter role id: ")
        delete_role(user_id)

    def update(self):
        role_id = input("Enter role id: ")
        name = input("Enter new name: ")
        update_role(role_id, name)

    def get_roles(self):
        list_roles()