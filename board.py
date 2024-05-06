from utils import const
from square import Square
from piece import *

class Board:
    def __init__(self):
         self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(const.COL)]
         self._createBoard()
         self._addPiece('white')
         self._addPiece('black')
    
    def _createBoard(self):
        for row in range(const.ROW):
            for col in range(const.COL):
                self.squares[row][col] = Square(row, col)

    def _addPiece(self,color):
        if color == 'white':
            row_pawn, row_other = (6,7)
        else:
            row_pawn, row_other = (1,0)

        # pawns
        for col in range(const.COL):
            self.squares[row_pawn][col] = Square(row_pawn,col, Pawn(color))

        # Knight
        self.squares[row_other][1] = Square(row_other,1, Knight(color))
        self.squares[row_other][6] = Square(row_other,6, Knight(color))

        # Bishop
        self.squares[row_other][2] = Square(row_other,1, Bishop(color))
        self.squares[row_other][5] = Square(row_other,6, Bishop(color))

        # Rook
        self.squares[row_other][0] = Square(row_other,0, Rook(color))
        self.squares[row_other][7] = Square(row_other,0, Rook(color))

        # King
        self.squares[row_other][4] = Square(row_other,4, King(color))
        
        # Queen
        self.squares[row_other][3] = Square(row_other,3, Queen(color))
    