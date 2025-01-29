from datetime import date
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.database import get_db
from database.models import Maintenance, Properties, Tenant

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Rental Management API"}


class TenantCreate(BaseModel):
    name: str
    email: str
    phone: str
    rent_due_date: date
    rent_amount: float

@app.post("/tenants/", response_model=TenantCreate)
async def create_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    db_tenant = Tenant(**tenant.dict())
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

@app.get("/tenants/{tenant_id}")
async def get_tenant(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant


@app.get("/tenants", response_model=List[dict])
async def get_all_tenants(db: Session = Depends(get_db)):
    tenants = db.query(Tenant).all()

    if not tenants:
        raise HTTPException(status_code=404, detail="No tenants found")

    tenant_data = []
    for tenant in tenants:
        # Get tenant's properties
        properties = db.query(Properties).filter(Properties.tenant_id == tenant.id).all()
        property_data = [
            {
                "id": prop.id,
                "address": prop.address,
                "bedrooms": prop.bedrooms,
                "bathrooms": prop.bathrooms,
                "monthly_rent": prop.monthly_rent,
                "available": prop.available,
            }
            for prop in properties
        ]

        # Get tenant's maintenance requests
        maintenance_requests = db.query(Maintenance).filter(Maintenance.tenant_id == tenant.id).all()
        maintenance_data = [
            {
                "id": maint.id,
                "description": maint.description,
                "status": maint.status.value,
                "created_at": maint.created_at,
                "updated_at": maint.updated_at,
                "completed_at": maint.completed_at,
                "property_id": maint.property_id,
            }
            for maint in maintenance_requests
        ]

        tenant_data.append(
            {
                "id": tenant.id,
                "name": tenant.name,
                "email": tenant.email,
                "phone": tenant.phone,
                "rent_due_date": tenant.rent_due_date,
                "rent_amount": tenant.rent_amount,
                "properties": property_data,
                "maintenance_requests": maintenance_data,
                "created_at": tenant.created_at,
                "updated_at": tenant.updated_at,
            }
        )

    return tenant_data
