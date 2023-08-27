from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

# Create an instance of the database
engine = create_engine("postgresql://postgres:postgres@localhost/mybalance", echo=True)


Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
