import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_SPEED = 8
BALL_SPEED = 5
START_LIVES = 3
FPS = 60

BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_W = 70
BRICK_H = 25
BRICK_GAP = 5
BRICK_TOP = 60
BRICK_LEFT = (SCREEN_WIDTH - (BRICK_COLS * BRICK_W + (BRICK_COLS - 1) * BRICK_GAP)) // 2
ROW_COLORS = ["red", "orange", "gold", "green", "turquoise"]

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 32)
big_font = pygame.font.SysFont("Times New Roman", 72)


def make_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            x = BRICK_LEFT + col * (BRICK_W + BRICK_GAP)
            y = BRICK_TOP + row * (BRICK_H + BRICK_GAP)
            bricks.append(pygame.Rect(x, y, BRICK_W, BRICK_H))
    return bricks


def brick_color(rect):
    row = (rect.y - BRICK_TOP) // (BRICK_H + BRICK_GAP)
    return pygame.Color(ROW_COLORS[row])


def new_game():
    paddle = pygame.Rect(0, SCREEN_HEIGHT - 40, 110, 14)
    paddle.centerx = SCREEN_WIDTH // 2
    ball_rect = pygame.Rect(0, 0, 14, 14)
    ball_pos = pygame.Vector2(paddle.centerx, paddle.top - 8)
    ball_rect.center = (round(ball_pos.x), round(ball_pos.y))
    return paddle, ball_rect, ball_pos, pygame.Vector2(0, 0), make_bricks(), 0, START_LIVES


paddle, ball_rect, ball_pos, ball_vel, bricks, score, lives = new_game()
state = "ready"  # "ready", "playing", "won", "lost"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            elif event.key == pygame.K_SPACE and state == "ready":
                ball_vel = pygame.Vector2(random.choice([-3, 3]), -BALL_SPEED)
                state = "playing"
            elif event.key == pygame.K_r and state in ("won", "lost"):
                paddle, ball_rect, ball_pos, ball_vel, bricks, score, lives = new_game()
                state = "ready"

    # Paddle movement
    if state in ("ready", "playing"):
        keys = pygame.key.get_pressed()
        paddle.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PADDLE_SPEED
        paddle.clamp_ip(screen.get_rect())

    if state == "ready":
        # Ball rides on the paddle until launched
        ball_pos.update(paddle.centerx, paddle.top - 8)
        ball_rect.center = (round(ball_pos.x), round(ball_pos.y))

    elif state == "playing":
        # Horizontal movement
        ball_pos.x += ball_vel.x
        ball_rect.centerx = round(ball_pos.x)
        if ball_rect.left <= 0:
            ball_rect.left = 0
            ball_pos.x = ball_rect.centerx
            ball_vel.x = abs(ball_vel.x)
        elif ball_rect.right >= SCREEN_WIDTH:
            ball_rect.right = SCREEN_WIDTH
            ball_pos.x = ball_rect.centerx
            ball_vel.x = -abs(ball_vel.x)
        hit = ball_rect.collidelist(bricks)
        if hit != -1:
            bricks.pop(hit)
            ball_vel.x *= -1
            score += 10

        # Vertical movement
        ball_pos.y += ball_vel.y
        ball_rect.centery = round(ball_pos.y)
        if ball_rect.top <= 0:
            ball_rect.top = 0
            ball_pos.y = ball_rect.centery
            ball_vel.y = abs(ball_vel.y)
        hit = ball_rect.collidelist(bricks)
        if hit != -1:
            bricks.pop(hit)
            ball_vel.y *= -1
            score += 10

        # Paddle bounce: angle depends on where the ball lands
        if ball_vel.y > 0 and ball_rect.colliderect(paddle):
            offset = (ball_rect.centerx - paddle.centerx) / (paddle.width / 2)
            ball_vel.x = offset * BALL_SPEED * 1.2
            ball_vel.y = -BALL_SPEED
            ball_rect.bottom = paddle.top
            ball_pos.y = ball_rect.centery

        # Ball fell off the bottom
        if ball_rect.top > SCREEN_HEIGHT:
            lives -= 1
            ball_vel = pygame.Vector2(0, 0)
            state = "lost" if lives <= 0 else "ready"

        if not bricks:
            state = "won"

    # Drawing
    screen.fill(pygame.Color("black"))
    for brick in bricks:
        pygame.draw.rect(screen, brick_color(brick), brick, border_radius=4)
    pygame.draw.rect(screen, pygame.Color("white"), paddle, border_radius=6)
    pygame.draw.ellipse(screen, pygame.Color("white"), ball_rect)

    hud = font.render(f"Score: {score}   Lives: {lives}", True, pygame.Color("white"))
    screen.blit(hud, (10, 10))

    if state == "ready":
        tip = font.render("Press SPACE to launch", True, pygame.Color("white"))
        screen.blit(tip, tip.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)))
    elif state in ("won", "lost"):
        msg = "You win!" if state == "won" else "Game over"
        color = pygame.Color("turquoise") if state == "won" else pygame.Color("red")
        text = big_font.render(msg, True, color)
        screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        sub = font.render("Press R to restart or X to quit", True, pygame.Color("white"))
        screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60)))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()