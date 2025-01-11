import sys

import pygame
from pygame.locals import *


pygame.init()

# Pre-defined game settings
GAME_SIZE = GAME_WIDTH, GAME_HEIGHT = 800, 800

FPS = 60
frame_per_second = pygame.time.Clock()



DISPLAY_SURFACE = pygame.display.set_mode(GAME_SIZE)
DISPLAY_SURFACE.fill("black")


class Square(pygame.Rect):
    width = DISPLAY_SURFACE.get_width() / 8
    def __init__(self, left, top, color="white"):
        super().__init__(left, top, self.width, self.width)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self)


class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            for j in range(8):
                self.board.append(Square(i * 100, j * 100, "white" if (i + j) % 2 == 0 else "darkgreen"))

    def draw(self):
        for column in self.board:
            for square in self.board:
                square.draw(DISPLAY_SURFACE)


# object instantiation
board = Board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # game updates


    # draw game
    board.draw()

    pygame.display.update()
    frame_per_second.tick(FPS)
