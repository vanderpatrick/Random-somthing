from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
load_dotenv()
DB_URL = os.environ['DATABASE_URL']
# Create an instance of the database
engine = create_engine(DB_URL, echo=True)


Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
