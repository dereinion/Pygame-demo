import pygame as pg
import random as rnd

# Initialize Pygame
pg.init()

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
enemyX = 300
enemyY = 200
enemyX_change = 0


def draw_player():
    screen.blit(playerIm, (round(playerX), round(playerY)))


def draw_enemy():
    screen.blit(enemyIm, (round(enemyX), round(enemyY)))


def get_color():
    return rnd.randint(150, 190)


def move_enemy():
    pass

playerChange = 0
# Game loop
running = True
while running:

    # Fill screen with color
    screen.fill((0, 128, 128))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                playerChange = -1
            if event.key == pg.K_RIGHT:
                playerChange = 1
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                playerChange = 0

    playerX += playerChange
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    draw_player()
    draw_enemy()
    if 100 < enemyX < 400:
        enemyX += 0.1
    else:
        enemyX = rnd.randint(100, 300)
    if 100 < enemyY < 400:
        enemyY += 0.1
    else:
        enemyY = rnd.randint(100, 300)

    pg.display.update()
