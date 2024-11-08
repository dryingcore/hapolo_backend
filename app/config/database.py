from sqlalchemy import create_engine, MetaData, Table
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")

engine = create_engine(
    f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

users_table = Table('users', metadata, autoload_with=engine)

try:
    with engine.connect() as connection:
        print("Database Connection Successful")
except Exception as e:
    print("Connection Failed:", e)
