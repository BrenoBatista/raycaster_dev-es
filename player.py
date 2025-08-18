import pygame
import math
from settings import *

class Player:
    def __init__(self):
        #defines the player innitial position being in the middle of the screen
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.radius = 3 #player size. He's a chubby boy.
        self.rotationAngle = 0

    def render(self, screen):
        #draw the player, wich, by hte way, is a dot.
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

        pygame.draw.line(screen, 
                         (255, 0, 0), 
                         (self.x, self.y), 
                         (self.x + math.cos(self.rotationAngle) * 50, self.y + math.sin(self.rotationAngle) * 50)
                         )
