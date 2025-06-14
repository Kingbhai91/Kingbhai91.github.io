import pygame
import random
import sys

pygame.init()

# स्क्रीन सेटअप
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Baahubali Attack Game")

# Clock
clock = pygame.time.Clock()

# Player की Image
player_img = pygame.image.load("baahubali.png")
player_img = pygame.transform.scale(player_img, (100, 150))
player_x = 350
player_y = 400
player_speed = 5

# Enemy की Image
enemy_img = pygame.image.load("enemy.png")  # Enemy image जो आपने बनाई है
enemy_img = pygame.transform.scale(enemy_img, (80, 80))
enemy_x = random.randint(0, WIDTH - 80)
enemy_y = 50
enemy_speed = 2

# Bullet Details
bullet_img = pygame.Surface((5, 10))
bullet_img.fill((255, 255, 0))  # Yellow bullet
bullets = []
bullet_speed = 7

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Black background
    clock.tick(60)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # गोली चलाओ (Spacebar दबाने पर)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + 50 - 2, player_y])  # bullet center से चले

    # Keys press handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 100:
        player_x += player_speed

    # Bullets Move
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Enemy Move
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - 80)

    # Collision Check
    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], 5, 10)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 80, 80)
        if bullet_rect.colliderect(enemy_rect):
            bullets.remove(bullet)
            enemy_x = random.randint(0, WIDTH - 80)
            enemy_y = 0  # दुबारा enemy ऊपर से आ जाए

    # Drawing
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))

    pygame.display.update()

pygame.quit()
sys.exit()
