from database.database import Base, engine  # Import the Base and engine from the database setup
from database.models import Tenant  # Import the Tenant model
from sqlalchemy import exc

# Create the tables in the database

try:
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
except exc.SQLAlchemyError as e:
    print(f"Error creating tables: {str(e)}")

