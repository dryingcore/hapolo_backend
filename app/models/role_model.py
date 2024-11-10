from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Role(Base):
    __tablename__ = 'roles'
    id = Column("id", Integer, primary_key=True)
    role_name = Column("role_name", String(255))