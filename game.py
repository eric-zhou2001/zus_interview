import random
from models.chessboard import ChessBoard, PieceType
from models.chess_piece import Color

SIZE = 8
REVERSE = 1

def convert_position_to_indices(rank: str, file: str) -> tuple[int, int]:
    if len(rank) != 1 or len(file) != 1:
        raise ValueError("Rank and file must be single characters")
    if rank not in '12345678' or file not in 'abcdefgh':
        raise ValueError("Invalid rank or file")
    
    rank_num = SIZE - int(rank) # Convert to respective positioning in array
    file_num = ord(file) - ord('a')  # Convert 'a'-'h' to 0-7
    return rank_num, file_num

def convert_indicies_to_position(rank: int, file: int) -> tuple[str, str]:
    if not (0 <= rank < SIZE) or not (0 <= file < SIZE):
        raise ValueError("Rank and file must be between 0 and 7")
    
    rank_str = str(SIZE - rank) # Flip again to retrieve original rank
    file_str = chr(file + ord('a'))  # Convert 0-7 to 'a'-'h'
    return rank_str, file_str

def main():
    print("Starting the chess game simulation...") 
    board = ChessBoard(SIZE)
    w_bishop_rank, w_bishop_file = convert_position_to_indices('3', 'c')  # c3
    b_rook_rank, b_rook_file = convert_position_to_indices('1', 'h')
    w_bishop = board.initialize_piece(PieceType.BISHOP, w_bishop_rank, w_bishop_file, Color.WHITE)
    b_rook = board.initialize_piece(PieceType.ROOK, b_rook_rank, b_rook_file, Color.BLACK)
    
    # Initial Board
    print("Initial Board:")
    print(board)
    captured = False
    i = 0
    while i < 15:
        rolls = random.choices(range(1, 7), k=2)
        heads = random.choice([True, False])
        board.move_piece(b_rook, heads, sum(rolls) * REVERSE)
        i += 1

        print(board)
        print("Rolls:", rolls)
        print("heads:", heads)
        print("Black Rook moved to:", convert_indicies_to_position(b_rook.rank, b_rook.file))
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

