from datetime import datetime
from uuid import uuid4

class GameSession:
    def __init__(self, player_id):
        self.session_id = str(uuid4())
        self.player_id = player_id
        self.start_time = datetime.now()
        self.end_time = None
        self.score = 0
        self.game_state = GameState()
        self.is_active = True

    def update_score(self, points):
        if self.is_active:
            self.score += points
            return self.score
        return None

    def end_session(self):
        if self.is_active:
            self.is_active = False
            self.end_time = datetime.now()
            return {
                'session_id': self.session_id,
                'player_id': self.player_id,
                'score': self.score,
                'duration': (self.end_time - self.start_time).seconds
            }
        return None

class GameState:
    def __init__(self):
        self.current_piece = None
        self.next_piece = None
        self.board = [[0 for _ in range(10)] for _ in range(20)]
        self.level = 1
        self.lines_cleared = 0
