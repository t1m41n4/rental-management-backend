import datetime
import enum

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    rent_due_date = Column(DateTime, nullable=False)
    rent_amount = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship to Maintenance Requests
    properties = relationship("Properties", back_populates="tenant")
    maintenance_requests = relationship("Maintenance", back_populates="tenant")


class Properties(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    monthly_rent = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=True)

    # Relationship to Maintenance Requests
    maintenance_requests = relationship("Maintenance", back_populates="property")
    tenant = relationship("Tenant", back_populates="properties")


class MaintenanceStatus(enum.Enum):
    Pending = "Pending"
    Completed = "Completed"
    InProgress = "In Progress"
    Cancelled = "Cancelled"
    NotRequired = "Not Required"


class Maintenance(Base):
    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), nullable=False)
    property_id = Column(Integer, ForeignKey("properties.id"), nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default=MaintenanceStatus.Pending.value)
    completed_at = Column(DateTime, nullable=True)

    # Relationships
    tenant = relationship("Tenant", back_populates="maintenance_requests")
    property = relationship("Properties", back_populates="maintenance_requests")

    def __repr__(self):
        return f"Maintenance(id={self.id}, tenant_id={self.tenant_id}, property_id={self.property_id}, description={self.description}, status={self.status})"
    
