from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

db_url = os.getenv("DB_URL")

engine = create_engine(db_url, echo=True)

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    with engine.connect() as connection:
        print("Database Connection Successful")
except Exception as e:
    print("Connection Failed:", e)
