import sys

import pygame

GAME_SIZE = (800, 800)

pygame.init()

DISPLAY_SURFACE = pygame.display.set_mode(GAME_SIZE)

FPS = pygame.time.Clock()
FPS.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()