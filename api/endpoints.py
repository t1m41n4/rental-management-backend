from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Tenant

router = APIRouter()


# API endpoint to get the rent due date for a specific tenant
@router.get("/rent-due/{tenant_id}")
async def get_rent_due(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if tenant:
        return {"rent_due_date": tenant.rent_due_date}
    return {"error": "Tenant not found"}

# Add more endpoints as necessary, e.g., for repairs or other rental management tasks
