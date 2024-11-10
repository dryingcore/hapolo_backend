from sqlalchemy import Column, Integer, String
from app.config.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    name = Column("name", String(255))
    email = Column("email", String(255))