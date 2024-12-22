import boto3
from botocore.exceptions import ClientError

class UserManager:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('Players')
        
    def create_player(self, username):
        player = Player(username)
        try:
            self.table.put_item(
                Item={
                    'player_id': player.player_id,
                    'username': player.username,
                    'created_at': player.created_at.isoformat(),
                    'stats': {
                        'games_played': 0,
                        'high_score': 0,
                        'total_score': 0
                    }
                },
                ConditionExpression='attribute_not_exists(username)'
            )
            return player
        except ClientError as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                raise ValueError(f"Username {username} already exists")
            raise

    def get_player(self, player_id):
        try:
            response = self.table.get_item(Key={'player_id': player_id})
            if 'Item' in response:
                return Player.from_dict(response['Item'])
            return None
        except ClientError as e:
            print(f"Error retrieving player: {e}")
            return None
