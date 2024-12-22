# src/api/routes.py
from fastapi import APIRouter, HTTPException
from typing import Dict
from ..game_logic.session import GameSession

router = APIRouter(prefix="/api/v1")

# Store active game sessions (in a real app, use a proper database)
game_sessions = {}

@router.post("/game/start")
async def start_game(player_id: str):
    session = GameSession(player_id)
    game_sessions[session.session_id] = session
    return {
        "session_id": session.session_id,
        "player_id": player_id,
        "message": "Game started successfully"
    }

@router.post("/game/{session_id}/move")
async def make_move(session_id: str, move: Dict):
    if session_id not in game_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    session = game_sessions[session_id]
    result = session.game_state.process_move(move)
    return {
        "success": True,
        "game_state": result
    }

@router.get("/game/{session_id}/state")
async def get_game_state(session_id: str):
    if session_id not in game_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    session = game_sessions[session_id]
    return session.game_state
