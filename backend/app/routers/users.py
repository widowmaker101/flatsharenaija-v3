from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, User, Token
from app.models.user import User as UserModel
from app.utils.auth import get_password_hash, verify_password, create_access_token
from app.database import SessionLocal

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    new_user = UserModel(email=user.email, hashed_password=hashed_password, preferences=user.preferences)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from dotenv import load_dotenv

load_dotenv()
sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

@router.post("/verify/{user_id}")
def send_verification_email(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Generate token (simple for example)
    verification_token = create_access_token({"sub": user.email, "verify": True}, timedelta(minutes=30))
    message = Mail(
        from_email='no-reply@flatsharenaija.com',
        to_emails=user.email,
        subject='Verify Your Email',
        html_content=f'<a href="http://localhost:3000/verify?token={verification_token}">Verify Email</a>'
    )
    try:
        sg.send(message)
        return {"detail": "Verification email sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
