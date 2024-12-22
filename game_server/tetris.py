import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
GRID_SIZE = 30  # Size of each grid square
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Purple
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (255, 0, 0),    # Red
    (0, 0, 255),    # Blue
    (255, 165, 0),  # Orange
]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Clock for controlling the game loop
clock = pygame.time.Clock()

class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def check_collision(grid, tetromino, offset_x=0, offset_y=0):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = tetromino.x + x + offset_x
                new_y = tetromino.y + y + offset_y
                if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or grid[new_y][new_x]:
                    return True
    return False

def merge_grid(grid, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[tetromino.y + y][tetromino.x + x] = tetromino.color

def clear_lines(grid):
    full_rows = [i for i, row in enumerate(grid) if all(row)]
    for i in full_rows:
        del grid[i]
        grid.insert(0, [0] * GRID_WIDTH)
    return len(full_rows)

def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x]:
                pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, GRAY, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def main():
    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    current_tetromino = Tetromino(random.choice(SHAPES), random.choice(COLORS))
    next_tetromino = Tetromino(random.choice(SHAPES), random.choice(COLORS))
    drop_timer = 0
    game_over = False
    score = 0

    while not game_over:
        screen.fill(BLACK)
        draw_grid(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(grid, current_tetromino, offset_x=-1):
                        current_tetromino.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(grid, current_tetromino, offset_x=1):
                        current_tetromino.x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(grid, current_tetromino, offset_y=1):
                        current_tetromino.y += 1
                elif event.key == pygame.K_UP:
                    current_tetromino.rotate()
                    if check_collision(grid, current_tetromino):
                        current_tetromino.rotate()
                        current_tetromino.rotate()
                        current_tetromino.rotate()

        # Automatic drop
        drop_timer += clock.get_rawtime()
        if drop_timer > 500:  # Drop speed in milliseconds
            drop_timer = 0
            if not check_collision(grid, current_tetromino, offset_y=1):
                current_tetromino.y += 1
            else:
                merge_grid(grid, current_tetromino)
                cleared_lines = clear_lines(grid)
                score += cleared_lines * 100
                current_tetromino = next_tetromino
                next_tetromino = Tetromino(random.choice(SHAPES), random.choice(COLORS))
                if check_collision(grid, current_tetromino):
                    game_over = True

        # Draw current tetromino
        for y, row in enumerate(current_tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, current_tetromino.color,
                                     ((current_tetromino.x + x) * GRID_SIZE,
                                      (current_tetromino.y + y) * GRID_SIZE,
                                      GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
# player.py
class Player:
    def __init__(self, player_id, username):
        self.player_id = player_id
        self.username = username
        self.current_game = None
        self.score = 0
        self.session_id = None

    def start_game(self):
        self.current_game = TetrisGame()
        self.score = 0

    def update_score(self, points):
        self.score += points
        # Trigger score update to database
# player.py
class Player:
    def __init__(self, player_id, username):
        self.player_id = player_id
        self.username = username
        self.current_game = None
        self.score = 0
        self.session_id = None

    def start_game(self):
        self.current_game = TetrisGame()
        self.score = 0

    def update_score(self, points):
        self.score += points
        # Trigger score update to database
# player.py
class Player:
    def __init__(self, player_id, username):
        self.player_id = player_id
        self.username = username
        self.current_game = None
        self.score = 0
        self.session_id = None

    def start_game(self):
        self.current_game = TetrisGame()
        self.score = 0

    def update_score(self, points):
        self.score += points
        # Trigger score update to database
# game_server/
│── main.py           # Main server application
│── game_logic/
│   ├── tetris.py     # Your existing Tetris game logic
│   └── player.py     # Player session management
│── models/
│   ├── user.py       # User profile management
│   └── leaderboard.py # Scoring and rankings
└── config/
    └── settings.py    # Configuration settings
