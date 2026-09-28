from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    role = Column(String(20), nullable=False) # 'citizen', 'driver', 'admin'
    state = Column(String(100))
    district = Column(String(100))
    city = Column(String(100))

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(String, primary_key=True, index=True)
    citizen_id = Column(Integer, ForeignKey("users.id"))
    driver_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    title = Column(String(255), nullable=False)
    complaint_type = Column(String(50), default="Garbage Dustbin")
    state = Column(String(100), nullable=False)
    district = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    photo_before = Column(Text, nullable=True)
    photo_after = Column(Text, nullable=True)
    status = Column(String(50), default="Pending") # 'Pending', 'In Progress', 'Completed'
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    resolved_at = Column(DateTime(timezone=True), nullable=True)