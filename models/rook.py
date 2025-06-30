from .chess_piece import ChessPiece

class Rook(ChessPiece):
    # This is assuming we can "hop" over other pieces for
    # optimizations; otherwise, we need to scan each spot
    def move(self, heads: bool, spaces: int) -> tuple[int, int]:
        if heads:
            # move up rank
            x = spaces % self.size
            if self.rank - x >= 0:
                self.rank -= x
            else:
                self.rank = self.size - (x - self.rank)
        else:
            # move right file
            self.file = (spaces + self.file) % self.size
        
        return self.rank, self.file

    # bit of a simplification, since what happens if there is
    # another object in the way?
    def capture(self, opponent: ChessPiece) -> bool:
        # Rook captures by moving to the same rank or file as the opponent
        return self.rank == opponent.rank or self.file == opponent.file
    
    def __str__(self):
        return f"R({super().__str__()})"