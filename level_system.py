import pygame
import sys

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Baahubali Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Load player image
player_img = pygame.image.load("baahubali.png")
player_img = pygame.transform.scale(player_img, (100, 150))
player_x = 350
player_y = 400
player_speed = 5

# Create enemy as a red box
enemy_img = pygame.Surface((80, 100))
enemy_img.fill((255, 0, 0))
enemy_x = 100
enemy_y = 100
enemy_speed = 3

# Game data
level = 1
enemy_defeated = False

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Black background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player within screen
    player_x = max(0, min(player_x, 800 - 100))

    # Move enemy
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= 800 - 80:
        enemy_speed *= -1

    # Simulate enemy defeat (you can replace this with real collision/bullet hit logic)
    if abs(player_x - enemy_x) < 50 and abs(player_y - enemy_y) < 50:
        level += 1
        enemy_speed += 1  # increase difficulty
        enemy_x = 100  # reset enemy position

    # Draw player and enemy
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Draw level text
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(level_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
