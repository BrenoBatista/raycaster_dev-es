import math, pygame
from settings import *
from Map import Map
from Player import Player

def normalizeAngle(angle):
    angle = angle % (2 * math.pi)
    if (angle <= 0):
        angle = (2 * math.pi) + angle
    return angle

def distanceBetween(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))


class Ray:
    def __init__(self, angle, player, map):
        self.rayAngle = normalizeAngle(angle)
        self.player: Player = player
        self.map: Map = map

        self.isFacingDown = self.rayAngle > 0 and self.rayAngle < math.pi
        self.isFacingUp = not self.isFacingDown
        self.isFacingRight = self.rayAngle < 0.5 * math.pi or self.rayAngle > 1.5 * math.pi
        self.isFacingLeft = not self.isFacingRight

        self.wallHitX = 0
        self.wallHitY = 0

        self.distance = 0

        self.color = 255

    
    def cast(self):
        # HORIZONTAL CHECKING
        foundHorizontalWall = False
        horizontalHitX = 0
        horizontalHitY = 0

        # The first intersection is the intersection where we need to offset by the player's position
        firstIntersectionX = None
        firstIntersectionY = None

        # finding y first
        if self.isFacingUp:
            firstIntersectionY = ((self.player.y // TILESIZE) * TILESIZE) - 0.01
        elif self.isFacingDown:
            firstIntersectionY = ((self.player.y // TILESIZE) * TILESIZE) + TILESIZE
        
        # finding x
        firstIntersectionX = self.player.x + (firstIntersectionY - self.player.y) / math.tan(self.rayAngle)

        # These variables will be used later
        nextHorizontalX = firstIntersectionX
        nextHorizontalY = firstIntersectionY

        # NOW, that we just figured out the first intersection, we need to continue checking
        # However, now the player won't go into our calculations

        xa = 0
        ya = 0


        # 1. Finding Ya
        if self.isFacingUp:
            ya = -TILESIZE
        elif self.isFacingDown:
            ya = TILESIZE
        
        # 2. Finding Xa
        xa = ya / math.tan(self.rayAngle)

        """
        if hit wall 
            store the position of the horizontal hit
        else
            add xa and ya to the current position
        """

        # while it is inside the window
        while (nextHorizontalX <= WINDOW_WIDTH and nextHorizontalX >= 0 and nextHorizontalY <= WINDOW_HEIGHT and nextHorizontalY >= 0):
            if self.map.hasWallAt(nextHorizontalX, nextHorizontalY):
                foundHorizontalWall = True
                horizontalHitX = nextHorizontalX
                horizontalHitY = nextHorizontalY
                break
            else:
                nextHorizontalX += xa
                nextHorizontalY += ya
            

        # VERTICAL CHECKING
        foundVerticalWall = False
        vertivalHitX = 0
        vertivalHitY = 0

        if self.isFacingRight:
            firstIntersectionX = ((self.player.x // TILESIZE) * TILESIZE) + TILESIZE
        elif self.isFacingLeft:
            firstIntersectionX = ((self.player.x // TILESIZE) * TILESIZE) - 0.01
        
        firstIntersectionY = self.player.y + (firstIntersectionX - self.player.x) * math.tan(self.rayAngle)
        
        nextVerticalX = firstIntersectionX
        nextVerticalY = firstIntersectionY

        # Now that we found the first intersection, we continue without the player, just as before

        # 1. Find Xa (just the width of the grid)

        if self.isFacingRight:
            xa = TILESIZE
        elif self.isFacingLeft:
            xa = -TILESIZE
        
        ya = xa * math.tan(self.rayAngle)

        # while it is inside the window
        while (nextVerticalX <= WINDOW_WIDTH and nextVerticalX >= 0 and nextVerticalY <= WINDOW_HEIGHT and nextVerticalY >= 0):
            if self.map.hasWallAt(nextVerticalX, nextVerticalY):
                foundVerticalWall = True
                vertivalHitX = nextVerticalX
                vertivalHitY = nextVerticalY
                break
            else:
                nextVerticalX += xa
                nextVerticalY += ya

        # # testing (temp)

        # self.wallHitX = horizontalHitX
        # self.wallHitY = horizontalHitY


        # DISTANCE CALCULATION

        horizontal_distance = 0
        verticalDistance = 0

        if foundHorizontalWall:
            horizontal_distance = distanceBetween(self.player.x, self.player.y, horizontalHitX, horizontalHitY)
        else:
            horizontal_distance = 999
        if foundVerticalWall:
            verticalDistance = distanceBetween(self.player.x, self.player.y, vertivalHitX, vertivalHitY)
        else:
            verticalDistance = 999
        

        if horizontal_distance < verticalDistance:
            self.wallHitX = horizontalHitX
            self.wallHitY = horizontalHitY
            self.distance = horizontal_distance
            self.color = 160
        else:
            self.wallHitX = vertivalHitX
            self.wallHitY = vertivalHitY
            self.distance = verticalDistance
            self.color = 255
        
        self.distance *= math.cos(self.player.rotationAngle - self.rayAngle)

        self.color *= (1 / self.distance) * 60
        if self.color > 255:
            self.color = 255
        elif self.color < 0:
            self.color = 0

    def render(self, screen):
        pygame.draw.line(screen, (255, 0, 0), 
                         (self.player.x, self.player.y), 
                         (self.wallHitX, self.wallHitY))