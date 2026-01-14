from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import paystack
from app.database import SessionLocal
from dotenv import load_dotenv
import os

load_dotenv()
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")  # Add to .env

paystack.api_key = PAYSTACK_SECRET_KEY

router = APIRouter(prefix="/payments", tags=["payments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/initialize")
async def initialize_payment(email: str, amount: float):  # Amount in NGN
    try:
        transaction = paystack.transaction.initialize(
            reference="unique_ref",  # Generate unique ref
            amount=int(amount * 100),  # Kobo
            email=email,
            callback_url="https://your-domain.com/verify"  # Update
        )
        return {"authorization_url": transaction['data']['authorization_url']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
