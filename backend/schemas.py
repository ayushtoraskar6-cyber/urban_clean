from pydantic import BaseModel, EmailStr
from typing import Optional

# --- USER SCHEMAS ---
class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str = "citizen"  # 'citizen', 'driver', 'admin'
    state: str
    district: str
    city: str

class UserCreate(UserBase):
    password: str  # Plain text password sent during registration

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


# --- COMPLAINT SCHEMAS ---
class ComplaintBase(BaseModel):
    title: str
    complaint_type: str = "Garbage Dustbin"
    state: str
    district: str
    city: str
    latitude: float
    longitude: float
    photo_before: Optional[str] = None

class ComplaintCreate(ComplaintBase):
    citizen_id: int

class ComplaintResponse(ComplaintBase):
    id: int
    status: str
    photo_after: Optional[str] = None

    class Config:
        from_attributes = True