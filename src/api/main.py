# src/api/main.py
from fastapi import FastAPI, WebSocket, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import jwt
from datetime import datetime, timedelta

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.post("/game/start")
async def start_game(player_id: str):
    session = game_manager.create_session(player_id)
    return {"session_id": session.session_id}

@app.post("/game/{session_id}/move")
async def make_move(session_id: str, move: Dict):
    session = game_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, message="Session not found")
    
    result = session.process_move(move)
    return result

@app.get("/game/{session_id}/state")
async def get_game_state(session_id: str):
    session = game_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=404, message="Session not found")
    
    return session.get_state()
