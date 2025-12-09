import math, pygame

def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if(angle < 0):
        angle = (2 * math.pi) + angle
    return angle

class Ray:
    def __init__(self, angle, player):
        self.rayAngle = normalizeAngle(angle)
        self.player = player
        
    def cast(self):
        pass
    
    def render(self, screen):
        start_pos = (int(self.player.x), int(self.player.y))
        end_pos = (
            int(self.player.x + math.cos(self.rayAngle) * 50),
            int(self.player.y + math.sin(self.rayAngle) * 50)
        )

        pygame.draw.line(screen, (255, 0, 0), start_pos, end_pos, 1)