from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.schemas.profile import ProfileCreate, Profile
from app.models.profile import Profile as ProfileModel
from app.database import SessionLocal
from imagekitio import ImageKit
from dotenv import load_dotenv
import os

load_dotenv()
imagekit = ImageKit(
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL_ENDPOINT")
)

router = APIRouter(prefix="/profiles", tags=["profiles"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Profile)
def create_profile(profile: ProfileCreate, user_id: int, db: Session = Depends(get_db)):
    new_profile = ProfileModel(**profile.dict(), user_id=user_id)
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@router.post("/upload-photo/{profile_id}")
async def upload_photo(profile_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    profile = db.query(ProfileModel).filter(ProfileModel.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    upload_result = imagekit.upload_file(
        file=file.file.read(),
        file_name=file.filename,
        options={"response_fields": ["url"]}
    )
    if upload_result['response'] is None:
        raise HTTPException(status_code=500, detail="Upload failed")
    profile.photo_url = upload_result['response']['url']
    db.commit()
    return {"photo_url": profile.photo_url}
