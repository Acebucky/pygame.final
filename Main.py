import os

from pygame.locals import *

from BaseClass import *
from process import process

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 1080, 720
# 4 variables ((screen,resolution),flags,color)
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

# clock for fps
clock = pygame.time.Clock()
FPS = 30
total_frames = 0  # keeps track of frames
background = pygame.image.load(os.path.join("images", "ForestA.jpg"))
bug = Bug(0, SCREENHEIGHT - 40, 40, 40, os.path.join("images", "Bug.gif"))

# ----------Main Program Loop-----------------
while True:
    process(bug, FPS, total_frames)
    # logic
    bug.motion(SCREENWIDTH, SCREENHEIGHT)
    Fly.update_all(SCREENWIDTH)
    BugProjectile.movement()
    total_frames += 1
    # logic
    # draw
    screen.blit(background, (0, 0))
    BaseClass.allsprites.draw(screen)
    BugProjectile.List.draw(screen)
    pygame.display.flip()
# draw



clock.tick(FPS)
