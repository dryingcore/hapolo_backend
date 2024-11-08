from app.config.database import session, users_table


def add_user():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    session.execute(users_table.insert().values(name=name, email=email))
    session.commit()
    print("User added successfully")

def delete_user():
    id = input("Enter user id: ")
    session.execute(users_table.delete().where(users_table.c.id == id))
    session.commit()
    print("User deleted successfully")

def update_user():
    id = input("Enter user id: ")
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    session.execute(users_table.update().where(users_table.c.id == id).values(name=name, email=email))
    session.commit()
    print("User updated successfully")

def list_users():
    users = session.execute(users_table.select()).all()
    for user in users:
        print(f"{user.id} - {user.name} - {user.email}")


def main_menu():
    while True:
        print("\n=== MENU ===")
        print("1. Add User")
        print("2. Delete User")
        print("3. List Users")
        print("4. Updated User")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            list_users()
        elif choice == "4":
            update_user()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()