# AWS Game Hackathon - Cloud Tetris

A modern implementation of the classic Tetris game powered by AWS services. This project demonstrates how to build a scalable game architecture using cloud services while maintaining the engaging gameplay of the original Tetris.

## Project Overview

This project implements a Tetris game with a twist - it leverages AWS services for backend operations, user management, and game state handling. The game maintains the classic Tetris mechanics while adding modern features like user authentication, score tracking, and real-time updates.

### Key Features

- Classic Tetris gameplay mechanics
- User authentication and session management
- Score tracking and persistence
- Real-time game state management
- AWS-powered backend infrastructure

### Architecture Components

- `game_server/`: Core game server implementation
  - `tetris.py`: Main Tetris game logic
- `src/`: Source code directory
  - `api/`: API endpoints and handlers
  - `auth/`: Authentication related functionality
  - `game_logic/`: Core game mechanics
    - `game_controller.py`: Game state controller
    - `session_manager.py`: Session handling
    - `tetromino.py`: Tetromino piece implementation
  - `models/`: Data models
    - `player.py`: Player entity model
    - `user_manager.py`: User management functionality
  - `utils/`: Utility functions and helpers
    - `monitoring.py`: Application monitoring

### AWS Services Used

- Amazon Cognito: User authentication and management
- Amazon DynamoDB: Game state and score persistence
- Amazon API Gateway: RESTful API endpoints
- AWS Lambda: Serverless compute for game logic
- Amazon CloudWatch: Application monitoring and logging

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/aws-hackathon.git
cd aws-hackathon
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure AWS credentials:
```bash
aws configure
```

4. Set up environment variables:
```bash
export AWS_REGION=your-region
export AWS_PROFILE=your-profile
```

## Running the Game

1. Start the game server:
```bash
python main.py
```

2. Access the game through your web browser at `http://localhost:8000`

## Development

### Project Structure
The project follows a modular architecture with clear separation of concerns:
- Game logic is isolated from AWS service integrations
- Authentication flow is handled separately from game mechanics
- Monitoring and utilities are maintained in dedicated modules

### Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## Testing

Run the test suite:
```bash
pytest tests/
```

## Security

- All user data is encrypted at rest and in transit
- Authentication is handled through Amazon Cognito
- Session management includes timeout and security measures
- API endpoints are protected with appropriate IAM roles

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built during the AWS Game Hackathon
- Inspired by the classic Tetris game
- Uses various AWS services for modern cloud implementation

