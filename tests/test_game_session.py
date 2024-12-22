# tests/test_game_session.py
import pytest
from src.game_logic.session import GameSession

def test_game_session_creation():
    session = GameSession("player123")
    assert session.player_id == "player123"
    assert session.is_active == True
    assert session.score == 0
    assert session.session_id is not None
    assert len(session.session_id) > 0
    assert session.start_time is not None
    assert session.end_time is None

def test_game_session_scoring():
    session = GameSession("player123")
    initial_score = session.score
    points_to_add = 100
    
    session.update_score(points_to_add)
    assert session.score == initial_score + points_to_add
    
    # Test multiple score updates
    session.update_score(50)
    assert session.score == initial_score + points_to_add + 50

def test_game_session_end():
    session = GameSession("player123")
    session.update_score(100)
    
    result = session.end_session()
    
    assert result is not None
    assert result['score'] == 100
    assert result['player_id'] == "player123"
    assert result['session_id'] == session.session_id
    assert result['duration'] >= 0
    assert session.is_active == False
    assert session.end_time is not None

def test_game_state_initialization():
    session = GameSession("player123")
    assert session.game_state is not None
    assert session.game_state.level == 1
    assert session.game_state.lines_cleared == 0
    assert len(session.game_state.board) == 20
    assert len(session.game_state.board[0]) == 10
    assert session.game_state.current_piece is None
    assert session.game_state.next_piece is None
