import math

TILESIZE = 32

ROWS = 10
COLS = 15

WINDOW_WIDTH = COLS * TILESIZE
WINDOW_HEIGHT = ROWS * TILESIZE

# FOV stands for field of view - basically the extent of area 
# # that can be seen by the player
#
# I'm setting the FOV in degrees - initially 60°(I may change this later)
# Problem is most of the functions use radians intead of degrees
# So teh formula here is (Radians = Degrees * (π / 180))
FOV = 60 * (math.pi / 180)

# RES - is the width of each rectangle
# Changing RES changes the ammount of rectangles in the screen
# The lower this value is the better everything looks
RES = 4 
NUM_RAYS = WINDOW_WIDTH / RES # Each rectangle is associated witha single ray