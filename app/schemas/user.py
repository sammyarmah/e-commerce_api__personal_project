from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    admin = "admin"
    customer = "customer"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole

class UserCreate(UserBase):
    pass

class User(UserCreate):
    id: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None