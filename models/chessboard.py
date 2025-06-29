from .bishop import Bishop
from .rook import Rook
from .chess_piece import ChessPiece, Color
from enum import Enum

class PieceType(Enum):
    BISHOP = Bishop
    ROOK = Rook

class ChessBoard:
    def __init__(self, size: int):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.pieces = {
            Color.WHITE: [],
            Color.BLACK: []
        }

    def initialize_piece(self, piece_type: PieceType, rank: int, file: int, color: Color) -> ChessPiece:
        piece_class = piece_type.value
        piece = piece_class(rank, file, self.size, color)
        self.place_piece(piece)
        self.pieces[color].append(piece)
        return piece

    def get_piece_at(self, rank: int, file: int) -> ChessPiece | None:
        if 0 <= rank < self.size and 0 <= file < self.size:
            return self.board[rank][file]
        else:
            raise ValueError("Position out of bounds")

    def place_piece(self, piece: ChessPiece):
        if self.board[piece.rank][piece.file] is not None:
            raise ValueError("Square already occupied")
        self.board[piece.rank][piece.file] = piece

    def move_piece(self, piece: ChessPiece, heads: bool, spaces: int):
        old_rank, old_file = piece.rank, piece.file
        new_rank, new_file = piece.move(heads, spaces)
        
        # Update board positions
        self.board[old_rank][old_file] = None
        if self.board[new_rank][new_file] is not None:
            raise ValueError("Cannot move to an occupied square")
        self.board[new_rank][new_file] = piece

    def is_captured(self, target: ChessPiece) -> bool:
        # Get the opposite color
        opposite_color = Color.BLACK if target.color == Color.WHITE else Color.WHITE
        for opponent in self.pieces[opposite_color]:
            if opponent.capture(target):
                return True
        return False

    def __str__(self):
        display = "White Pieces: " + ", ".join(str(p) for p in self.pieces[Color.WHITE]) + "\n"
        display += "Black Pieces: " + ", ".join(str(p) for p in self.pieces[Color.BLACK]) + "\n"
        display += "Board:\n"
        # Add file labels (numbers) at the top
        display += "   " + " ".join(str(i) for i in range(1, self.size+1)) + "\n"
        for idx, row in enumerate(self.board):
            # Add rank labels (letters) at the start of each row
            rank_label = chr(ord('a') + idx)
            display += f"{rank_label}  " + " ".join(['.' if cell is None else str(cell) for cell in row]) + "\n"
        return display