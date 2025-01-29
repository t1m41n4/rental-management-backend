from fastapi import Depends, FastAPI, HTTPException
from database.models import Tenant
from sqlalchemy.orm import Session
from database.database import get_db
from typing import List

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Rental Management API"}

@app.get("/rent-due/{tenant_id}")
async def get_rent_due(tenant_id: int, db: Session = Depends(get_db)):
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return {
        "tenant_id": tenant_id,
        "rent_due_date": tenant.rent_due_date,
        "rent_amount": tenant.rent_amount
    }