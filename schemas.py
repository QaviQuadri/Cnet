from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from datetime import datetime
from pydantic import BaseModel

class CrisisReportBase(BaseModel):
    name: str
    phone: str
    location: str
    message: str

class CrisisReport(CrisisReportBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ----------------- User Schemas -----------------
class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


# ----------------- Crisis Report Schemas -----------------
class CrisisReportBase(BaseModel):
    title: str
    description: str
    location: str
    severity: Optional[str] = "Medium"

class CrisisReportCreate(CrisisReportBase):
    user_id: int

class CrisisReportResponse(CrisisReportBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True