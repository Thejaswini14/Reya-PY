import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 6
START_LIVES = 3
WIN_SCORE = 15
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coin Dodge")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 32)
big_font = pygame.font.SysFont("Times New Roman", 72)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(pygame.Color("turquoise"))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.invincible_until = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_SPEED
        self.rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * PLAYER_SPEED
        self.rect.clamp_ip(screen.get_rect())
        # Blink while invincible after a hit
        blinking = pygame.time.get_ticks() < self.invincible_until
        self.image.set_alpha(120 if blinking and (pygame.time.get_ticks() // 100) % 2 else 255)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.Color("gold"), (12, 12), 12)
        pygame.draw.circle(self.image, pygame.Color("orange"), (12, 12), 12, 3)
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(40, SCREEN_HEIGHT - self.rect.height)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((36, 36))
        self.image.fill(pygame.Color("red"))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([0, SCREEN_WIDTH - 36])
        self.rect.y = random.randint(40, SCREEN_HEIGHT - 36)
        self.vx = random.choice([-1, 1]) * speed
        self.vy = random.choice([-1, 1]) * speed

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.vy *= -1
        self.rect.clamp_ip(screen.get_rect())


def new_game():
    player = Player()
    coin = Coin()
    enemies = pygame.sprite.Group(Enemy(3))
    return player, coin, enemies, 0, START_LIVES


player, coin, enemies, score, lives = new_game()
state = "playing"  # "playing", "won", "lost"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            elif event.key == pygame.K_r and state != "playing":
                player, coin, enemies, score, lives = new_game()
                state = "playing"

    if state == "playing":
        player.update()
        enemies.update()
        now = pygame.time.get_ticks()

        if player.rect.colliderect(coin.rect):
            score += 1
            coin.respawn()
            # Add a new enemy every 3 coins, slightly faster each time
            if score % 3 == 0:
                enemies.add(Enemy(3 + score // 3))
            if score >= WIN_SCORE:
                state = "won"

        if now >= player.invincible_until:
            if pygame.sprite.spritecollideany(player, enemies):
                lives -= 1
                player.invincible_until = now + 1500
                if lives <= 0:
                    state = "lost"

    # Drawing
    screen.fill(pygame.Color("midnightblue"))
    screen.blit(coin.image, coin.rect)
    enemies.draw(screen)
    screen.blit(player.image, player.rect)

    hud = font.render(f"Score: {score}/{WIN_SCORE}   Lives: {lives}", True, pygame.Color("white"))
    screen.blit(hud, (10, 5))

    if state != "playing":
        msg = "You win!" if state == "won" else "Game over"
        color = pygame.Color("turquoise") if state == "won" else pygame.Color("red")
        text = big_font.render(msg, True, color)
        screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)))
        sub = font.render("Press R to restart or X to quit", True, pygame.Color("white"))
        screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
