import pygame
from Raycaster import Raycaster
from settings import *
from Map import Map
from Player import *

screen =  pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

map = Map()

player = Player()

clock = pygame.time.Clock()
raycaster = Raycaster(player, map)

backgroundImage = pygame.image.load("background.png")

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            pygame.quit()
            exit()
            
    player.update()

    screen.blit(backgroundImage, (0, 0))
    
    #map.render(screen)
    #player.render(screen)
    raycaster.castAllRays()

    raycaster.render(screen)
    pygame.display.update()