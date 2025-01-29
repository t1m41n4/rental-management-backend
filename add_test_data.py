from datetime import date, datetime

from database.database import SessionLocal
from database.models import Maintenance, MaintenanceStatus, Properties, Tenant


def add_test_data():
    """Insert test data for tenants, properties, and maintenance requests."""
    db = SessionLocal()

    try:
        current_time = datetime.now()

        # Add properties
        property_1 = Properties(
            address="123 Elm Street",
            bedrooms=3,
            bathrooms=2,
            monthly_rent=1500,
            available=True,
            created_at=current_time,
            updated_at=current_time
        )
        property_2 = Properties(
            address="456 Oak Avenue",
            bedrooms=2,
            bathrooms=1,
            monthly_rent=1100,
            available=True,
            created_at=current_time,
            updated_at=current_time
        )

        db.add_all([property_1, property_2])
        db.commit()

        # Add tenants
        tenant_1 = Tenant(
            name="John Doe",
            email="john@example.com",
            phone="555-0123",
            rent_due_date=date(2025, 2, 1),
            rent_amount=1200,
            created_at=current_time,
            updated_at=current_time
        )
        tenant_2 = Tenant(
            name="Jane Smith",
            email="jane@example.com",
            phone="555-0456",
            rent_due_date=date(2025, 2, 5),
            rent_amount=1400,
            created_at=current_time,
            updated_at=current_time
        )

        db.add_all([tenant_1, tenant_2])
        db.commit()

        # Add maintenance requests
        maintenance_1 = Maintenance(
            tenant_id=tenant_1.id,
            property_id=property_1.id,
            description="Leaky faucet in kitchen",
            status=MaintenanceStatus.Pending.value,
            created_at=current_time,
            updated_at=current_time
        )
        maintenance_2 = Maintenance(
            tenant_id=tenant_2.id,
            property_id=property_2.id,
            description="Broken heater",
            status=MaintenanceStatus.InProgress.value,
            created_at=current_time,
            updated_at=current_time
        )

        db.add_all([maintenance_1, maintenance_2])
        db.commit()

        print("Test data added successfully.")

    except Exception as e:
        print(f"Error adding test data: {e}")
        db.rollback()

    finally:
        db.close()


if __name__ == "__main__":
    add_test_data()
