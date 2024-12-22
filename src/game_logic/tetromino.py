# src/game_logic/tetromino.py
from enum import Enum
from typing import List, Tuple

class TetrominoType(Enum):
    I = 'I'
    O = 'O'
    T = 'T'
    S = 'S'
    Z = 'Z'
    J = 'J'
    L = 'L'

class Tetromino:
    SHAPES = {
        TetrominoType.I: [
            [1, 1, 1, 1]
        ],
        TetrominoType.O: [
            [1, 1],
            [1, 1]
        ],
        TetrominoType.T: [
            [0, 1, 0],
            [1, 1, 1]
        ],
        # Add other shapes...
    }

    def __init__(self, type: TetrominoType):
        self.type = type
        self.shape = self.SHAPES[type]
        self.x = 0
        self.y = 0
        self.rotation = 0

    def rotate(self) -> List[List[int]]:
        """Rotate the tetromino 90 degrees clockwise"""
        return list(zip(*self.shape[::-1]))

    def get_positions(self) -> List[Tuple[int, int]]:
        """Get all occupied positions"""
        positions = []
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    positions.append((self.x + x, self.y + y))
        return positions
