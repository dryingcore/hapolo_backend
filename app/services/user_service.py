from app.config.database import session
from app.models.user_model import User

def new_user(name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print("User added successfully")

def delete_user(user_id):
    session.query(User).filter(User.id == user_id).delete()
    session.commit()
    print("User deleted successfully")

def list_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

def update_user(user_id, name, email):
    session.query(User).filter(User.id == user_id).update({"name": name, "email": email})
    session.commit()
    print("User updated successfully")