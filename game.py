import pygame
import sys

from utils import const

class Game:
    def __init__(self):
        pass

    def showBackground(self,surface):
        for row in range(const.ROW):
            for col in range(const.COL):
                if (row+col)%2 == 0:
                    pygame.draw.rect(surface,const.WHITE,(col*const.Square_Size,row*const.Square_Size,const.Square_Size,const.Square_Size))
                else:
                    pygame.draw.rect(surface,const.BLACK,(col*const.Square_Size,row*const.Square_Size,const.Square_Size,const.Square_Size))