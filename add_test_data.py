from database.database import SessionLocal
from database.models import Tenant
from datetime import date


def add_test_tenant():
    db = SessionLocal()
    try:
        test_tenant = Tenant(
            name="John Doe",
            email="john@example.com",
            phone="555-0123",
            rent_due_date=date(2025, 2, 1),
            rent_amount=1200.00,
            created_at=date.today(),
            updated_at=date.today()
        )
        db.add(test_tenant)
        db.commit()
        print("Test tenant added successfully")
    except Exception as e:
        print(f"Error adding test tenant: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    add_test_tenant()
