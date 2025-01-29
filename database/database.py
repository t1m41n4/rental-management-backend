from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your actual database credentials
DATABASE_URL = "postgresql://rental_user:password@localhost/rentaldb"


# Create engine to connect to the PostgreSQL database
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal is a session factory, used to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all database models
Base = declarative_base()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
