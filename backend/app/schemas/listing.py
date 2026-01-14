from pydantic import BaseModel
from typing import List, Optional

class ListingBase(BaseModel):
    location: str
    price_ngn: float
    amenities: List[str]
    description: Optional[str] = None

class ListingCreate(ListingBase):
    pass

class Listing(ListingBase):
    id: int
    user_id: int
    country: str

    class Config:
        from_attributes = True
