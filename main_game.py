import pygame
import sys

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Baahubali Game")

# Load Baahubali image
player_img = pygame.image.load("baahubali.png")
player_img = pygame.transform.scale(player_img, (100, 150))
player_x = 350
player_y = 400
player_speed = 5

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player on screen
    if player_x < 0:
        player_x = 0
    if player_x > 700:
        player_x = 700  # 800 - 100 (image width)

    screen.blit(player_img, (player_x, player_y))
    pygame.display.update()

pygame.quit()
sys.exit()
