from utils import const
from square import Square

class Board:
    def __init__(self):
         self.squares = [[None]*const.COL for _ in range(const.ROW)]

         self._createBoard()
    
    def _createBoard(self):
        for row in range(const.ROW):
            for col in range(const.COL):
                if (row+col)%2 == 0:
                    color = const.WHITE
                else:
                    color = const.BLACK
                self.squares[row][col] = Square(row,col,color)

    def _addPiece(self,color):
        pass