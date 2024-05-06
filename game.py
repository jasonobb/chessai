import pygame
import sys
from board import Board
from utils import const
from square import Square

class Game:
    def __init__(self):
        self.board = Board()

    def showBackground(self,surface):
        for row in range(const.ROW):
            for col in range(const.COL):
                if (row+col)%2 == 0:
                    pygame.draw.rect(surface,const.WHITE,(col*const.Square_Size,row*const.Square_Size,const.Square_Size,const.Square_Size))
                else:
                    pygame.draw.rect(surface,const.BLACK,(col*const.Square_Size,row*const.Square_Size,const.Square_Size,const.Square_Size))

    
    def showPieces(self,surface):
       for row in range(const.ROW):
            for col in range(const.COL):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col*const.Square_Size + const.Square_Size//2, row*const.Square_Size + const.Square_Size//2
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img,piece.texture_rect)