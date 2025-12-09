import pygame
from raycaster import Raycaster
from settings import *
from map import Map
from player import *

screen =  pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

map = Map()

player = Player()

clock = pygame.time.Clock()
raycaster = Raycaster(player)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            pygame.quit()
            exit()
            
    player.update()

    screen.fill((0, 0, 0))
    
    map.render(screen)

    player.render(screen)
    raycaster.castAllRays()

    raycaster.render(screen)
    pygame.display.update()