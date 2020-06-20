import pygame as pg
import random as rnd

# Initialize Pygame
pg.init()

# Create a window
screen = pg.display.set_mode((1920, 1080))

# Title and icons
pg.display.set_caption('Space invaders')
icon = pg.image.load('ufo.png')
pg.display.set_icon(icon)

playerIm = pg.image.load('spaceship.png')
playerX = 370
playerY = 300


def draw_player():
    screen.blit(playerIm, (playerX, playerY))

def get_color():
    return rnd.randint(1, 255)

# Game loop
running = True
while running:

    # Fill screen with color
    screen.fill((get_color(), get_color(), get_color()))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        draw_player()
    pg.display.update()
