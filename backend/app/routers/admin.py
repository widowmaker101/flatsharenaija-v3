from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import User
from app.models.user import User as UserModel
from app.database import SessionLocal
from app.utils.auth import oauth2_scheme  # Assume admin check

router = APIRouter(prefix="/admin", tags=["admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Simple admin check (expand with roles)
def get_current_admin(token: str = Depends(oauth2_scheme)):
    # Verify token and check if admin
    return True  # Placeholder

@router.get("/users", response_model=List[User])
def list_users(db: Session = Depends(get_db), current_admin: bool = Depends(get_current_admin)):
    return db.query(UserModel).all()
