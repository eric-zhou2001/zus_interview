import random
from models.chessboard import ChessBoard, PieceType
from models.chess_piece import Color

SIZE = 8

def main():
    print("Starting the chess game simulation...") 
    board = ChessBoard(SIZE)
    w_bishop = board.initialize_piece(PieceType.BISHOP, 2, 2, Color.WHITE)
    b_rook = board.initialize_piece(PieceType.ROOK, 7, 0, Color.BLACK)
    
    captured = False
    i = 0
    while i < 15:
        rolls = random.choices(range(1, 7), k=2)
        heads = random.choice([True, False])
        board.move_piece(b_rook, heads, sum(rolls))
        i += 1

        print(board)
        print("Rolls:", rolls)
        print("heads:", heads)
        captured = board.is_captured(b_rook)

        if captured:
            break

    
    print("Number of moves:", i)
    if captured:
        print("Black Rook is captured by White Bishop!")
    else:
        print("Black Rook survived the game!")

if __name__ == "__main__":
    main()

