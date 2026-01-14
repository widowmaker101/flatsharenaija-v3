from sqlalchemy import Column, Integer, String, Float, ARRAY
from app.database import Base

class Listing(Base):
    __tablename__ = "listings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)  # Foreign key to User
    location = Column(String)  # e.g., "Lagos"
    price_ngn = Column(Float)
    amenities = Column(ARRAY(String))  # List of amenities, e.g., ["wifi", "kitchen"]
    description = Column(String)
    country = Column(String, default="ng")
