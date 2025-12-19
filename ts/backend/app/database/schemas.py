from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Optional[str] = "corporate"
    org_name: str

# class UserOut(BaseModel):
#     id: int
#     name: str
#     email: EmailStr
#     role: str
#     org_name: str
#     created_at: datetime
#     class Config:
#         orm_mode = True

# class Token(BaseModel):
#     access_token: str
#     token_type: str = "bearer"

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str
    org_name: str
    created_at: datetime
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    user: UserOut



class LoginData(BaseModel):
    email: EmailStr
    password: str

class DocumentCreate(BaseModel):
    doc_type: str
    doc_number: Optional[str] = None
    file_url: Optional[str] = None
    hash: Optional[str] = None
    issued_at: Optional[datetime] = None   # <-- THIS MUST BE OPTIONAL

class DocumentOut(BaseModel):
    id: int
    owner_id: int
    doc_type: str
    doc_number: Optional[str]
    file_url: Optional[str]
    hash: Optional[str]
    issued_at: Optional[datetime]
    created_at: datetime
    org_name: str
    class Config:
        orm_mode = True