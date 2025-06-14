
import pygame
import sys
import random

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Baahubali Game - Enemy Aircraft")

# Load Baahubali image
player_img = pygame.image.load("baahubali.png")
player_img = pygame.transform.scale(player_img, (100, 150))
player_x = 350
player_y = 400
player_speed = 5

# Enemy setup
enemy_img = pygame.image.load("enemy.png")  # Provide your own image enemy.png
enemy_img = pygame.transform.scale(enemy_img, (60, 60))

num_enemies = 5
enemies = []
for _ in range(num_enemies):
    enemies.append({
        "x": random.randint(0, 740),
        "y": random.randint(-600, 0),
        "speed": random.randint(2, 5)
    })

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 700:
        player_x += player_speed

    screen.blit(player_img, (player_x, player_y))

    # Move and draw enemies
    for enemy in enemies:
        enemy["y"] += enemy["speed"]
        if enemy["y"] > 600:
            enemy["y"] = random.randint(-200, -50)
            enemy["x"] = random.randint(0, 740)
        screen.blit(enemy_img, (enemy["x"], enemy["y"]))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
