import pygame
import sys

from utils import const
from game import Game

class MAIN:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
        pygame.display.set_caption("Jason Chess")
        self.game = Game()

    def run(self):

        game = self.game
        screen = self.screen

        game.showBackground(screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()


main = MAIN()

main.run()