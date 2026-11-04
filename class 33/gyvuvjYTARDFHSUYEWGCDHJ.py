# Step 1: Import pygame to build the game, and random to place sprites at random positions.

# Step 2: Define constants for SCREEN_WIDTH, SCREEN_HEIGHT, MOVEMENT_SPEED, and FONT_SIZE.

# Step 3: Initialize Pygame using pygame.init().

# Step 4: Load "bg.jpg" and scale it to fill the screen using pygame.image.load() and pygame.transform.scale().

# Step 5: Load a font using pygame.font.SysFont("Times New Roman", FONT_SIZE).

# Step 6: Create a Sprite class that inherits from pygame.sprite.Sprite.

# Step 7: In the constructor, call super().__init__(), fill the sprite's image with dodgerblue, then draw a colored rectangle on top of it using pygame.draw.rect().

# Step 8: Get the sprite's rect from its image using self.image.get_rect().

# Step 9: Define a move() method that updates the sprite's x and y position, using max() and min() to keep it inside the screen.

# Step 10: Create the game window with set_mode(), and set its title with set_caption().

# Step 11: Create a Group with all_sprites = pygame.sprite.Group().

# Step 12: Create sprite1 (black) at a random position, and add it to the group.

# Step 13: Create sprite2 (red) at a random position, and add it to the group.

# Step 14: Set up running and won as True/False control variables, and create a clock.

# Step 15: Start the main loop, checking pygame.QUIT or the X key to exit.

# Step 16: If the game isn't won yet, check the arrow keys with get_pressed(), and move sprite1 using the move() method.

# Step 17: Check for a collision between sprite1 and sprite2 using colliderect() - if they touch, remove sprite2 from the group and set won = True.

# Step 18: Draw the background, then all remaining sprites, onto the screen each frame.

# Step 19: If won, render "You win!" and blit it centered on the screen using get_width() and get_height().

# Step 20: Update the display with flip(), limit the frame rate with clock.tick(90), and call pygame.quit() once the loop ends.




import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
FONT_SIZE = 72
IMAGE_PATH = "/Users/teju/Downloads/iXTL4fXGZtLebDkpuM8reslZmo9bvbJ2PEhRRn56_thumbnail_jT5C.jpg"

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

try:
    background_image = pygame.image.load(IMAGE_PATH).convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except (FileNotFoundError, pygame.error):
    background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image.fill(pygame.Color("darkslategray"))

font = pygame.font.SysFont("Times New Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))

    def randomize_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)


all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color("black"), 50, 50)
sprite2 = Sprite(pygame.Color("red"), 50, 50)
sprite1.randomize_position()
sprite2.randomize_position()
while sprite1.rect.colliderect(sprite2.rect):  # avoid spawning on top of each other
    sprite2.randomize_position()

all_sprites.add(sprite1, sprite2)

running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(dx, dy)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You win!", True, pygame.Color("turquoise"))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
                               (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame.display.flip()   # now runs every frame
    clock.tick(30)

pygame.quit()