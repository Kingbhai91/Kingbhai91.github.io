import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Baahubali Game - Step 3")

clock = pygame.time.Clock()
player_img = pygame.image.load("baahubali.png")
player_rect = player_img.get_rect(midbottom=(400, 550))
player_speed = 5
bullets = []

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.speed = -10

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player_rect.centerx, player_rect.top))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # Boundaries
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > 800:
        player_rect.right = 800

    screen.blit(player_img, player_rect)

    for bullet in bullets[:]:
        bullet.move()
        bullet.draw()
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    pygame.display.flip()
    clock.tick(60)
