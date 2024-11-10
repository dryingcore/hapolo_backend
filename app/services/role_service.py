from app.config.database import session
from app.models.role_model import Role

def new_role(name):
    role = Role(role_name=name)
    session.add(role)
    session.commit()
    print("Role added successfully")

def list_roles():
    roles = session.query(Role).all()
    for role in roles:
        print(f"ID: {role.id}, Name: {role.role_name}")

def delete_role(role_id):
    session.query(Role).filter(Role.id == role_id).delete()
    session.commit()
    print("Role deleted successfully")

def update_role(role_id, name):
    session.query(Role).filter(Role.id == role_id).update({"role_name": name})
    session.commit()
    print("Role updated successfully")