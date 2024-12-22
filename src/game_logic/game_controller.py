class GameController:
    def __init__(self, session_manager, user_manager):
        self.session_manager = session_manager
        self.user_manager = user_manager

    async def start_game(self, player_id):
        """Start a new game for a player"""
        player = self.user_manager.get_player(player_id)
        if player:
            session_id = self.session_manager.create_session(player_id)
            return {
                'status': 'success',
                'session_id': session_id,
                'message': 'Game started successfully'
            }
        return {
            'status': 'error',
            'message': 'Player not found'
        }

    async def update_game(self, session_id, game_action):
        """Process a game action"""
        session = self.session_manager.get_active_session(session_id)
        if session:
            # Process game action and return updated state
            result = session.process_action(game_action)
            return {
                'status': 'success',
                'game_state': result
            }
        return {
            'status': 'error',
            'message': 'Session not found'
        }

    async def end_game(self, session_id):
        """End a game session"""
        result = self.session_manager.end_session(session_id)
        if result:
            return {
                'status': 'success',
                'final_score': result['score'],
                'duration': result['duration']
            }
        return {
            'status': 'error',
            'message': 'Session not found or already ended'
        }
