# src/game_logic/game.py
from typing import Optional
from .tetromino import Tetromino, TetrominoType
import random

class TetrisGame:
    def __init__(self, width: int = 10, height: int = 20):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.current_piece: Optional[Tetromino] = None
        self.next_piece: Optional[Tetromino] = None
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self._spawn_piece()

    def _spawn_piece(self) -> bool:
        """Spawn a new piece at the top of the board"""
        if self.next_piece is None:
            self.next_piece = Tetromino(random.choice(list(TetrominoType)))
        
        self.current_piece = self.next_piece
        self.next_piece = Tetromino(random.choice(list(TetrominoType)))
        
        # Center the piece
        self.current_piece.x = (self.width - len(self.current_piece.shape[0])) // 2
        self.current_piece.y = 0
        
        # Check if game is over
        if self._check_collision():
            self.game_over = True
            return False
        return True

    def _check_collision(self, offset_x: int = 0, offset_y: int = 0) -> bool:
        """Check if current piece collides with anything"""
        if not self.current_piece:
            return False

        for pos_x, pos_y in self.current_piece.get_positions():
            new_x = pos_x + offset_x
            new_y = pos_y + offset_y

            if (new_x < 0 or new_x >= self.width or 
                new_y >= self.height or
                (new_y >= 0 and self.board[new_y][new_x])):
                return True
        return False

    def move(self, direction: str) -> bool:
        """Move the current piece"""
        if self.game_over or not self.current_piece:
            return False

        offset_x = {'left': -1, 'right': 1}.get(direction, 0)
        offset_y = 1 if direction == 'down' else 0

        if not self._check_collision(offset_x, offset_y):
            self.current_piece.x += offset_x
            self.current_piece.y += offset_y
            return True
        
        # If moving down and collision detected, lock the piece
        if direction == 'down':
            self._lock_piece()
            self._clear_lines()
            self._spawn_piece()
        return False

    def _lock_piece(self) -> None:
        """Lock the current piece in place"""
        if not self.current_piece:
            return

        for x, y in self.current_piece.get_positions():
            if y >= 0:
                self.board[y][x] = 1

    def _clear_lines(self) -> None:
        """Clear completed lines and update score"""
        lines_to_clear = []
        for y in range(self.height):
            if all(self.board[y]):
                lines_to_clear.append(y)

        for y in lines_to_clear:
            del self.board[y]
            self.board.insert(0, [0] * self.width)

        cleared = len(lines_to_clear)
        if cleared:
            self.lines_cleared += cleared
            self.score += self._calculate_score(cleared)
            self._update_level()

    def _calculate_score(self, lines: int) -> int:
        """Calculate score based on lines cleared"""
        base_points = {1: 100, 2: 300, 3: 500, 4: 800}
        return base_points.get(lines, 0) * self.level

    def _update_level(self) -> None:
        """Update level based on lines cleared"""
        self.level = 1 + self.lines_cleared // 10
