import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Ensure the player stays within the screen boundaries
        self.rect.x = max(0, min(WIDTH - 50, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - 50, self.rect.y))

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid Overlapping Objects")

# Create players
player1 = Player(RED, 100, 100)
player2 = Player(BLUE, 200, 200)

all_sprites = pygame.sprite.Group()
all_sprites.add(player1, player2)

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update sprites
    all_sprites.update()

    # Check for collisions and adjust positions
    if pygame.sprite.collide_rect(player1, player2):
        player1.rect.x -= 5
        player1.rect.y -= 5

    # Draw everything
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
