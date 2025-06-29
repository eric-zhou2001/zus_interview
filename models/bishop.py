from .chess_piece import ChessPiece

class Bishop(ChessPiece):
    def move(self, heads: bool, spaces: int) -> tuple[int, int]:
        # TBD
        pass

    # bit of a simplification, since what happens if there is
    # another object in the way?
    def capture(self, opponent: ChessPiece) -> bool:
        # Bishop captures by moving to the same diagonal as the opponent
        return abs(self.rank - opponent.rank) == abs(self.file - opponent.file)
    
    def __str__(self):
        return "B"