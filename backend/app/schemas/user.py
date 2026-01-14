from pydantic import BaseModel
from typing import Dict, Optional

class UserBase(BaseModel):
    email: str
    preferences: Optional[Dict] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    country: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
