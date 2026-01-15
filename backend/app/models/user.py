from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    preferences = Column(JSON)  # For AI matching: lifestyle, etc.
    country = Column(String, default="ng")
    is_verified = Column(Boolean, default=False)
