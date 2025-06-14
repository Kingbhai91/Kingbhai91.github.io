
import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Baahubali Attack Game")
clock = pygame.time.Clock()

player_img = pygame.image.load("baahubali.png")
player_img = pygame.transform.scale(player_img, (100, 150))
player_x, player_y = 350, 400
player_speed = 5

enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (80, 80))
enemy_x = random.randint(0, WIDTH - 80)
enemy_y = 50
enemy_speed = 2

bullet_img = pygame.Surface((5, 10))
bullet_img.fill((255, 255, 0))
bullets = []
bullet_speed = 7

running = True
while running:
    screen.fill((0, 0, 0))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append([player_x + 50 - 2, player_y])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 100:
        player_x += player_speed

    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)

    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - 80)

    for bullet in bullets[:]:
        bullet_rect = pygame.Rect(bullet[0], bullet[1], 5, 10)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 80, 80)
        if bullet_rect.colliderect(enemy_rect):
            bullets.remove(bullet)
            enemy_x = random.randint(0, WIDTH - 80)
            enemy_y = 0

    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))

    pygame.display.update()

pygame.quit()
sys.exit()
