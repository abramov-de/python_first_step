import pygame
import random

WIDTH = 800
HEIGHT = 650
FPS = 30

# Set a color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(50, 50)
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.rigth = 0

# Creating game and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving square.")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()