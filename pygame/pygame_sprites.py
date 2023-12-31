import pygame

WIDTH = 800
HEIGHT = 650
FPS = 30

# Set color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            # self.rect.right = 0
            self.rect.speedX *= -1
            self.rect.x += self.rect.speedX


# Create game and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Square.")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # Keep right speed
    clock.tick(FPS)
    # Input process (event)
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Updating
    all_sprites.update()

    # Rendering
    screen.fill(WHITE)
    all_sprites.draw(screen)
    # Flip screen after drawing
    pygame.display.flip()

pygame.quit()
