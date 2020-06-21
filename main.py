import pygame as pg
import random as rnd

# Initialize Pygame
pg.init()

# Background
background = pg.image.load('background.png')

# Create a window
screen = pg.display.set_mode((800, 600))

# Title and icons
pg.display.set_caption('Space invaders')
icon = pg.image.load('ufo.png')
pg.display.set_icon(icon)

# Player position and image
playerIm = pg.image.load('spaceship.png')
playerX = 370
playerY = 425

# Enemy position and image
enemyIm = pg.image.load('enemy.png')
enemyX = rnd.randint(0, 800)
enemyY = rnd.randint(50, 150)
enemyX_change = 4
enemyY_change = 40


def draw_player():
    screen.blit(playerIm, (round(playerX), round(playerY)))


def draw_enemy():
    screen.blit(enemyIm, (round(enemyX), round(enemyY)))


def get_color():
    return rnd.randint(150, 190)


playerChange = 0
# Game loop
running = True
while running:

    # Fill screen with color
    screen.fill((0, 128, 128))

    # Set background
    screen.blit(background, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerChange = -15
            if event.key == pg.K_RIGHT:
                playerChange = 15
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerChange = 0

    draw_player()
    playerX += playerChange

    # Checking boundaries for player
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # Checking boundaries for enemies
    if enemyX < 0:
        enemyX = 0
    elif enemyX > 736:
        enemyX = 736

    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change

    draw_enemy()
    enemyX += enemyX_change

    pg.display.update()
