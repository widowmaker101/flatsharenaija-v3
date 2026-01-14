from fastapi import APIRouter
import socketio

router = APIRouter(prefix="/messages", tags=["messages"])

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

@sio.event
async def connect(sid, environ):
    print("User connected:", sid)

@sio.event
async def disconnect(sid):
    print("User disconnected:", sid)

@sio.event
async def message(sid, data):
    # Broadcast message to room or user; example broadcast
    await sio.emit('message', data, skip_sid=sid)  # Echo back

# Mount socketio in main.py later
