from uuid import uuid4
from datetime import datetime

class Player:
    def __init__(self, username):
        self.player_id = str(uuid4())
        self.username = username
        self.created_at = datetime.now()
        self.current_session = None
        self.stats = PlayerStats()
        
    def start_game(self):
        """Initialize a new game session for the player"""
        if self.current_session is None:
            self.current_session = GameSession(self.player_id)
            return self.current_session
        return None

    def end_game(self):
        """End the current game session and update stats"""
        if self.current_session:
            final_score = self.current_session.get_score()
            self.stats.update_stats(final_score)
            self.current_session = None

class PlayerStats:
    def __init__(self):
        self.games_played = 0
        self.high_score = 0
        self.total_score = 0
        self.last_played = None
        
    def update_stats(self, score):
        self.games_played += 1
        self.total_score += score
        self.high_score = max(self.high_score, score)
        self.last_played = datetime.now()
