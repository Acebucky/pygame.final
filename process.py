import random
import sys

import pygame

import BaseClass


def process(bug, FPS, total_frames):
    # processes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        BaseClass.Bug.going_right = True
        bug.image = pygame.image.load("images/Bug.gif")
        bug.velx = 5
    elif keys[pygame.K_a]:
        BaseClass.Bug.going_right = False
        bug.image = pygame.image.load("images/Bugflipped.gif")
        bug.velx = -5
    else:
        bug.velx = 0

    if keys[pygame.K_w]:
        bug.jumping = True

    if keys[pygame.K_SPACE]:
        p = BaseClass.BugProjectile(bug.rect.x, bug.rect.y, 43, 25, "images/projectiles/Fire.gif")
        if BaseClass.Bug.going_right:
            p.velx = 8
        else:
            p.image = pygame.transform.flip(p.image, True, False)
            p.velx = -8

    spawn(FPS, total_frames)
    collisions()


# processes
def spawn(FPS, total_frames):
    four_seconds = FPS * 4

    if total_frames % four_seconds == 0:

        r = random.randint(1, 2)
        x = 1
        if r == 2:
            x = 640 - 40

        BaseClass.Fly(x, 130, 40, 35, "images/Fly.gif")


def collisions():
    for fly in BaseClass.Fly.List:

        Fly_proj = pygame.sprite.spritecollide(fly, BaseClass.BugProjectile.List, True)
        if len(Fly_proj) > 0:
            for hit in Fly_proj:
                fly.health -= fly.half_health
