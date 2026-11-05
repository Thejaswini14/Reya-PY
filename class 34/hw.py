import pygame
import random
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Collision Game!")
WHITE = (255, 255, 255)
BLUE = (0, 100, 250)
RED = (250, 50, 50)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
score = 0
player_rect = pygame.Rect(400, 300, 40, 40)
player_speed = 5
enemy_rects = []
for i in range(7):
    enemy_x = random.randint(0, WIDTH - 30)
    enemy_y = random.randint(0, HEIGHT - 30)
    new_enemy = pygame.Rect(enemy_x, enemy_y, 30, 30)
    enemy_rects.append(new_enemy)
score_font = pygame.font.SysFont("Arial", 30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
    for enemy in enemy_rects:
        if player_rect.colliderect(enemy):
            score = score + 1
            enemy.x = random.randint(0, WIDTH - 30)
            enemy.y = random.randint(0, HEIGHT - 30)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    for enemy in enemy_rects:
        pygame.draw.rect(screen, RED, enemy)
    score_text = score_font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (20, 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()
