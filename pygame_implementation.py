import sys

import pygame


pygame.init()

DISPLAY_SURFACE = pygame.display.set_mode(GAME_SIZE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()