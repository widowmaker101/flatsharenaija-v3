from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from transformers import pipeline

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    message: str

pipe = pipeline("text-generation", model="distilgpt2")  # Small local model

@router.post("/")
def chat(request: ChatRequest):
    try:
        response = pipe(request.message, max_new_tokens=100)[0]['generated_text']
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
