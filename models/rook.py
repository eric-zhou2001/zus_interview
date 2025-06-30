from .chess_piece import ChessPiece

class Rook(ChessPiece):
    def move(self, heads: bool, spaces: int) -> tuple[int, int]:
        if heads:
            if spaces < 0:
                # move down rank
                self.rank = self.size - (((spaces + self.rank) * -1) % self.size)
            else:
                # move up rank
                self.rank = (spaces + self.rank) % self.size
        else:
            if spaces < 0:
                # move left file
                self.file = self.size - (((spaces + self.file) * -1) % self.size)
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