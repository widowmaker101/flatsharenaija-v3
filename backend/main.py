from fastapi import FastAPI
from app.routers import users, listings, matching

app = FastAPI(title="FlatShareNaija API", description="AI-powered flat share backend for Nigeria")

app.include_router(users.router)
app.include_router(listings.router)
app.include_router(matching.router)
app.include_router(payments.router)

@app.get("/")
def root():
    return {"message": "Welcome to FlatShareNaija API"}

# SocketIO for messaging
from app.routers.messages import sio
from socketio import ASGIApp
app.mount("/ws", ASGIApp(sio))
