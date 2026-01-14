from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.database import SessionLocal
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()
AI_API_KEY = os.getenv("AI_API_KEY")

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
    candidates = db.query(UserModel).filter(UserModel.country == user.country, UserModel.id != user_id).all()
    matches = []
    async with aiohttp.ClientSession() as session:
        for candidate in candidates:
            prompt = f"Compare roommate compatibility (0-100 score): User1 prefs: {user.preferences}, User2 prefs: {candidate.preferences}."
            async with session.post("https://api.openai.com/v1/chat/completions",
                                    headers={"Authorization": f"Bearer {AI_API_KEY}"},
                                    json={"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]}) as resp:
                data = await resp.json()
                try:
                    score = int(data['choices'][0]['message']['content'].split()[0])
                    if score > 70:
                        matches.append({"candidate_id": candidate.id, "score": score})
                except:
                    pass  # Skip invalid responses
    return {"matches": matches}
