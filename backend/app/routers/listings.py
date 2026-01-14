from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.listing import ListingCreate, Listing
from app.models.listing import Listing as ListingModel
from app.database import SessionLocal

router = APIRouter(prefix="/listings", tags=["listings"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Listing)
def create_listing(listing: ListingCreate, user_id: int, db: Session = Depends(get_db)):  # Assume user_id from auth
    new_listing = ListingModel(**listing.dict(), user_id=user_id)
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return new_listing

@router.get("/", response_model=List[Listing])
def read_listings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    listings = db.query(ListingModel).offset(skip).limit(limit).all()
    return listings

@router.get("/{listing_id}", response_model=Listing)
def read_listing(listing_id: int, db: Session = Depends(get_db)):
    listing = db.query(ListingModel).filter(ListingModel.id == listing_id).first()
    if listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

@router.put("/{listing_id}", response_model=Listing)
def update_listing(listing_id: int, listing: ListingCreate, db: Session = Depends(get_db)):
    db_listing = db.query(ListingModel).filter(ListingModel.id == listing_id).first()
    if db_listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    for key, value in listing.dict().items():
        setattr(db_listing, key, value)
    db.commit()
    db.refresh(db_listing)
    return db_listing

@router.delete("/{listing_id}")
def delete_listing(listing_id: int, db: Session = Depends(get_db)):
    db_listing = db.query(ListingModel).filter(ListingModel.id == listing_id).first()
    if db_listing is None:
        raise HTTPException(status_code=404, detail="Listing not found")
    db.delete(db_listing)
    db.commit()
    return {"detail": "Listing deleted"}
