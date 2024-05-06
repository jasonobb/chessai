import pygame
from utils import const

class Square:
    def __init__(self,row,col,color, piece = None):
        self.row = row
        self.col = col
        self.color = color
        self.x = self.col*const.Square_Size
        self.y = self.row*const.Square_Size
        self.width = const.Square_Size
        self.height = const.Square_Size
        self.piece = piece

    def draw(self,surface):
        pygame.draw.rect(surface,self.color,(self.x,self.y,self.width,self.height))

    def __repr__(self): 
        return f'Row: {self.row}, Col: {self.col}, Color: {self.color}'