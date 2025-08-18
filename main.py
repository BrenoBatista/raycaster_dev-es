import pygame
from settings import *
from map import Map
from player import *

screen =  pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

map = Map()
player = Player()

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            pygame.quit()
            exit()


    screen.fill((0, 0, 0))
    
    map.render(screen)

    player.render(screen)

    pygame.display.update()