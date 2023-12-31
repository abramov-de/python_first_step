import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Set color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create game and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Correct FPS check
    clock.tick(FPS)
    # Event (process) input
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Rendering
    screen.fill(BLACK)
    # Screen flip after rendering
    pygame.display.flip()

pygame.quit()
