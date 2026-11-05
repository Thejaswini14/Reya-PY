
import pygame
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(
    "Wildlife Information Display"
)
background_image = pygame.transform.scale(
    pygame.image.load("background.png").convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

wildlife_image = pygame.transform.scale(
    pygame.image.load("tiger.png").convert_alpha(),
    (220, 220)
)
wildlife_rect = wildlife_image.get_rect(
    center=(
        SCREEN_WIDTH // 2,
        SCREEN_HEIGHT // 2 - 30
    )
)
heading_font = pygame.font.Font(None, 42)
fact_font = pygame.font.Font(None, 28)
heading_text = heading_font.render(
    "Wildlife Spotlight: Tiger",
    True,
    pygame.Color("black")
)
heading_rect = heading_text.get_rect(
    center=(SCREEN_WIDTH // 2, 45)
)
fact_text = fact_font.render(
    "Tigers are powerful wild cats.",
    True,
    pygame.Color("black")
)
fact_rect = fact_text.get_rect(
    center=(SCREEN_WIDTH // 2, 420)
)
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(
            background_image,
            (0, 0)
        )

        display_surface.blit(
            wildlife_image,
            wildlife_rect
        )
        display_surface.blit(
            heading_text,
            heading_rect
        )
 
        display_surface.blit(
            fact_text,
            fact_rect
        )
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()
import pygame
import random

CELL = 20
COLS = 40
ROWS = 30
SCREEN_WIDTH = COLS * CELL
SCREEN_HEIGHT = ROWS * CELL
START_SPEED = 8      # moves per second
MAX_SPEED = 20

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 32)
big_font = pygame.font.SysFont("Times New Roman", 72)

DIRECTIONS = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}


def place_food(snake):
    free = [(x, y) for x in range(COLS) for y in range(ROWS) if (x, y) not in snake]
    return random.choice(free)


def new_game():
    snake = [(COLS // 2, ROWS // 2), (COLS // 2 - 1, ROWS // 2), (COLS // 2 - 2, ROWS // 2)]
    return snake, (1, 0), [], place_food(snake), 0


def draw_cell(pos, color, inset=1):
    rect = pygame.Rect(pos[0] * CELL + inset, pos[1] * CELL + inset,
                       CELL - inset * 2, CELL - inset * 2)
    pygame.draw.rect(screen, color, rect, border_radius=5)


snake, direction, queued, food, score = new_game()
high_score = 0
alive = True
running = True
move_timer = 0

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            elif event.key == pygame.K_r and not alive:
                snake, direction, queued, food, score = new_game()
                alive = True
            elif event.key in DIRECTIONS and alive:
                new_dir = DIRECTIONS[event.key]
                last = queued[-1] if queued else direction
                # Can't reverse into yourself; keep at most 2 queued turns
                if new_dir != (-last[0], -last[1]) and new_dir != last and len(queued) < 2:
                    queued.append(new_dir)

    if alive:
        speed = min(START_SPEED + score // 3, MAX_SPEED)
        move_timer += dt
        if move_timer >= 1000 / speed:
            move_timer = 0
            if queued:
                direction = queued.pop(0)

            head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
            ate = head == food
            body = snake if ate else snake[:-1]   # tail moves away unless we grow

            if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in body:
                alive = False
                high_score = max(high_score, score)
            else:
                snake.insert(0, head)
                if ate:
                    score += 1
                    if len(snake) == COLS * ROWS:   # board completely full
                        alive = False
                        high_score = max(high_score, score)
                    else:
                        food = place_food(snake)
                else:
                    snake.pop()

    # Drawing
    screen.fill(pygame.Color("gray10"))
    for x in range(COLS):
        for y in range(ROWS):
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, pygame.Color("gray14"),
                                 (x * CELL, y * CELL, CELL, CELL))

    draw_cell(food, pygame.Color("red"), inset=3)
    for i, segment in enumerate(snake):
        draw_cell(segment, pygame.Color("turquoise") if i == 0 else pygame.Color("limegreen"))

    hud = font.render(f"Score: {score}   Best: {high_score}", True, pygame.Color("white"))
    screen.blit(hud, (10, 5))

    if not alive:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        text = big_font.render("Game over", True, pygame.Color("red"))
        screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)))
        sub = font.render("Press R to restart or X to quit", True, pygame.Color("white"))
        screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)))

    pygame.display.flip()

pygame.quit()