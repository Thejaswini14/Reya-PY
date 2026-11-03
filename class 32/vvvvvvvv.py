# Step 1: Import pygame to build the game, and random to generate random colors, directions, and positions.

# Step 2: Initialize Pygame using pygame.init().

# Step 3: Create two custom event IDs, SPRITE_COLOR_CHANGE_EVENT and BACKGROUND_COLOR_CHANGE_EVENT, using pygame.USEREVENT + 1 and + 2.

# Step 4: Define background colors (BLUE, LIGHTBLUE, DARKBLUE) and sprite colors (YELLOW, MAGENTA, ORANGE, WHITE) using pygame.Color().

# Step 5: Create a Sprite class that inherits from pygame.sprite.Sprite.

# Step 6: In the constructor, call super().__init__(), then create self.image as a Surface, fill it with color, and create self.rect from it.

# Step 7: Give the sprite a random starting velocity using self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])].

# Step 8: Define an update() method that moves the sprite using self.rect.move_ip(self.velocity).

# Step 9: Inside update(), check whether the sprite has touched the left/right or top/bottom edges, and reverse the matching velocity value if so.

# Step 10: If a boundary was touched, post both SPRITE_COLOR_CHANGE_EVENT

# and BACKGROUND_COLOR_CHANGE_EVENT using pygame.event.post().

# Step 11: Define a change_color() method on the sprite that fills it with a random sprite color, and a change_background_color() function that picks a random background color.

# Step 12: Create a Group with all_sprites_list = pygame.sprite.Group(), create one Sprite named sp1 at a random position, and add it to the group.

# Step 13: Create the game window with set_mode((500, 400)), set its title with set_caption(), and fill it with the initial background color.

# Step 14: Start the main loop, checking pygame.QUIT to exit, and the two elif branches to handle the custom events.

# Step 15: Each pass, update and redraw every sprite in the group using all_sprites_list.update(), screen.fill(), and all_sprites_list.draw(screen), then refresh with flip() and limit speed with clock.tick(240).

# Step 16: When the loop ends, close Pygame using pygame.quit().





import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color("blue")
LIGHTBLUE = pygame.Color("lightblue")
DARKBLUE = pygame.Color("darkblue")
YELLOW = pygame.Color("yellow")
MAGENTA = pygame.Color("magenta")
ORANGE = pygame.Color("orange")
WHITE = pygame.Color("white")
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        if self.rect.left < 0 or self.rect.right > 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        else:
            boundary_hit = False
        if self.rect.top < 0 or self. rect.bottom > 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))
def change_background_color():
    return random.choice([BLUE, LIGHTBLUE, DARKBLUE])
all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(YELLOW, 50, 50)
sp1.rect.x = random.randint(0, 450)
sp1.rect.y = random.randint(0, 350)
all_sprites_list.add(sp1)
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Bouncing sprite with Color Change")
screen.fill(BLUE)
exit = False
bg_color = BLUE
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            bg_color = change_background_color()

    all_sprites_list.update()      
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)                
