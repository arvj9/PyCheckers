import sys

import pygame


pygame.init()

# Pre-defined game settings
GAME_WIDTH = 800
GAME_HEIGHT = 800
GAME_SIZE = (GAME_WIDTH, GAME_HEIGHT)

FPS = 60
frame_per_second = pygame.time.Clock()

# Pre-defined colors -> rgb(0-255, 0-255, 0-255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAY_SURFACE = pygame.display.set_mode(GAME_SIZE)
DISPLAY_SURFACE.fill(BLACK)

class Square(pygame.Rect):
    def __init__(self, left: float, top: float, width: float, color = WHITE):
        super().__init__(left, top, width, width)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self)


# object instantiation
SQUARE = Square(0, 0, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # game updates


    # draw game
    SQUARE.draw(DISPLAY_SURFACE)

    pygame.display.update()
    frame_per_second.tick(FPS)
