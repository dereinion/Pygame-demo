import pygame as pg

# Initialize Pygame
pg.init()

# Create a window
screen = pg.display.set_mode((800, 640))

# Game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
