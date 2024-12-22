import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # AWS Configuration
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    
    # DynamoDB Tables
    PLAYERS_TABLE = os.getenv('PLAYERS_TABLE', 'Players')
    SESSIONS_TABLE = os.getenv('SESSIONS_TABLE', 'GameSessions')
    
    # Game Configuration
    MAX_PLAYERS = 100
    SESSION_TIMEOUT = 3600  # 1 hour in seconds
    
    # API Configuration
    API_VERSION = '1.0'
    
settings = Settings()
