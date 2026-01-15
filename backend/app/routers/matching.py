from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.database import SessionLocal
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')  # Local embedding model

router = APIRouter(prefix="/matching", tags=["matching"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}")
async def get_matches(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_prefs_str = str(user.preferences)
    user_embedding = model.encode(user_prefs_str)
    candidates = db.query(UserModel).filter(UserModel.country == user.country, UserModel.id != user_id).all()
    matches = []
    for candidate in candidates:
        candidate_prefs_str = str(candidate.preferences)
        candidate_embedding = model.encode(candidate_prefs_str)
        score = util.cos_sim(user_embedding, candidate_embedding)[0][0].item() * 100  # 0-100 score
        if score > 70:
            matches.append({"candidate_id": candidate.id, "score": int(score)})
    return {"matches": matches}
