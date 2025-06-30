from enum import Enum

class Color(Enum):
    WHITE = "white"
    BLACK = "black"

class ChessPiece():
    def __init__(self, rank: int, file: int, size: int, color: Color):
        self.rank = rank
        self.file = file
        self.size = size
        self.color = color

    def move(self, heads: bool, spaces: int) -> tuple[int, int]:
        raise NotImplementedError("This method should be overridden by subclasses")
        
    def capture(self, opponent: 'ChessPiece') -> bool:
        raise NotImplementedError("This method should be overridden by subclasses")

    def __str__(self):
        if self.color == Color.WHITE:
            color_code = "W"
        else:
            color_code = "B"
        return color_code