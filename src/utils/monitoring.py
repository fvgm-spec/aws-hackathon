# src/utils/monitoring.py
import boto3
import logging
from datetime import datetime

class GameMetrics:
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')
        self.logger = logging.getLogger(__name__)
        self.setup_logging()

    def setup_logging(self):
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def log_game_start(self, session_id: str, player_id: str):
        self.logger.info(f"Game started - Session: {session_id}, Player: {player_id}")
        self._put_metric("GameStarts", 1)

    def log_game_end(self, session_id: str, score: int, duration: int):
        self.logger.info(
            f"Game ended - Session: {session_id}, Score: {score}, Duration: {duration}s"
        )
        self._put_metric("GameEnds", 1)
        self._put_metric("GameScore", score)
        self._put_metric("GameDuration", duration)

    def _put_metric(self, name: str, value: float):
        try:
            self.cloudwatch.put_metric_data(
                Namespace="TetrisGame",
                MetricData=[
                    {
                        'MetricName': name,
                        'Value': value,
                        'Unit': 'Count',
                        'Timestamp': datetime.utcnow()
                    }
                ]
            )
        except Exception as e:
            self.logger.error(f"Error putting metric {name}: {str(e)}")
