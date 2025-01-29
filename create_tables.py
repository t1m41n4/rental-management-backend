from sqlalchemy import exc

from database.database import (  # Import the Base and engine from the database setup
    Base, engine)
from database.models import Properties, Tenant  # Import the Tenant model

# Create the tables in the database

try:
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
except exc.SQLAlchemyError as e:
    print(f"Error creating tables: {str(e)}")

