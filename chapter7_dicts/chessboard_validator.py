STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'ww', 'd1': 'wQ', 'e1': 'wK', 'f1': 'ww',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}


def isValidChessBoard(starting_chess_dict: dict): # my-py: ignore-errors; type: ignore
    
    validChessBoard = True
    
    # Check the basic total number.
    if len(starting_chess_dict) == 32:
        print("So far, the right number of pieces appears.")
        white_pieces = []
        black_pieces = []
        misc_pieces = []
        for piece_name in starting_chess_dict.values():
            if 'b' in piece_name:
                black_pieces.append(piece_name)
            elif 'w' in piece_name:
                white_pieces.append(piece_name)
            else:
                misc_pieces.append(piece_name)
        
        # Check the pieces are not in nonsense places
        validChessGrid = []
        for y in '87654321':
            for x in 'abcdefgh':
                validChessGrid.append(x+y)
        
        for position in starting_chess_dict.keys():
            if position not in validChessGrid:
                print("But are you sure all those squares are valid in chess?")
                validChessBoard = False
                break
                
            else:
                continue   
         
        if validChessBoard:
            print("And all your starting positions are at least valid on a chess board!")    
                
        # Check pieces neatly divide into 16 black and 16 white, with no rogue pieces.
        if len(black_pieces) == 16 and len(white_pieces) == 16:
            print("And the appropriate colour divison of 16 white - 16 black is present.")
        else:
            print("But there aren't 16 white and 16 black pieces.")
            print(f"White pieces: {len(white_pieces)}.")
            print(f"Black pieces: {len(black_pieces)}.")
            print(f"And miscellaneous pieces?! There's {len(misc_pieces)}. Please fix.")
            validChessBoard = False
        
        # And now, that they each contain a king.
        if white_pieces.count('wK') == 1 and black_pieces.count('bK') == 1:
            print("There's exactly 1 White King and 1 Black King - congrats!")
            
        else:
            print("But do the White & Black King exist as 1 a-piece in their sets? Check...")
            validChessBoard = False
        
            
        # And now the 8 pawns a piece
        if white_pieces.count('wP') == 8 and black_pieces.count('bP') == 8:
            print("And there's 8 pawns in each colour - nice!")
        else:
            print("But there's something wrong with your pawns... Check.")
            validChessBoard = False
        
            
        
        
    else:
        print("Your chessboard does not have the necessary amount of starting pieces.")
        print("It is therefore NOT a valid chessboard.")
        validChessBoard = False
    
    return f"All in all - is this a valid chessboard? {validChessBoard}!"
    
    
isValidChessBoard(STARTING_PIECES)



INSTRUCTIONS = """
Chess Dictionary Validator
In this chapter, we used the dictionary value {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'} to represent a chessboard. 
Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on whether the board is valid.

A valid board will have exactly one black king and exactly one white king. 
Each player can have at most 16 pieces, of which only eight can be pawns, and all pieces must be on a valid square from '1a' to '8h'. 
That is, a piece can’t be on square '9z'. 
The piece names should begin with either a 'w' or a 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. 
This function should detect when a bug has resulted in an improper chessboard. 
(This isn’t an exhaustive list of requirements, but it is close enough for this exercise.)
"""