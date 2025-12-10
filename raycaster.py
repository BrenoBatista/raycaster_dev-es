import pygame
from settings import *
from Ray import Ray

class Raycaster:
    def __init__(self, player, map):
        self.rays = []
        self.player = player
        self.map = map
        
    def castAllRays(self):
        self.rays = []
        rayAngle = (self.player.rotationAngle - FOV/2)
        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)
            
            rayAngle += FOV / NUM_RAYS
            
    def render(self, screen):
        
        i = 0
        for ray in self.rays:
            #ray.render(screen)
            
            lineHeight = (32 / ray.distance) * 415
            
            drawBegin = (WINDOW_HEIGHT / 2) - (lineHeight / 2)
            drawEnd = lineHeight
            
            pygame.draw.rect(screen, (ray.color, ray.color, ray.color), (i * RES, drawBegin, RES, drawEnd))
            
            i += 1