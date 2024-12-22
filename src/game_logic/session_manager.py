import boto3
from datetime import datetime

class GameSessionManager:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.sessions_table = self.dynamodb.Table('GameSessions')
        self.active_sessions = {}

    def create_session(self, player_id):
        """Create a new game session"""
        session = GameSession(player_id)
        self.active_sessions[session.session_id] = session
        
        # Store session in DynamoDB
        self.sessions_table.put_item(
            Item={
                'session_id': session.session_id,
                'player_id': player_id,
                'start_time': session.start_time.isoformat(),
                'status': 'active'
            }
        )
        return session.session_id

    def end_session(self, session_id):
        """End a game session and save results"""
        if session_id in self.active_sessions:
            session = self.active_sessions[session_id]
            session_data = session.end_session()
            
            # Update session in DynamoDB
            self.sessions_table.update_item(
                Key={'session_id': session_id},
                UpdateExpression='SET end_time = :end_time, score = :score, status = :status',
                ExpressionAttributeValues={
                    ':end_time': datetime.now().isoformat(),
                    ':score': session_data['score'],
                    ':status': 'completed'
                }
            )
            
            del self.active_sessions[session_id]
            return session_data
        return None

    def get_active_session(self, session_id):
        """Get an active game session"""
        return self.active_sessions.get(session_id)
