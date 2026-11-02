# Step 1: Define a main() function, initialize pygame, and create a 500x500 window with a caption.

# Step 2: Store five named colors in a colors dictionary, and set current_color to white.

# Step 3: Set the sprite's starting x, y position and its width and height, then create a clock to control frame rate.

# Step 4: Start the main loop, checking pygame.event.get() for the pygame.QUIT event.

# Step 5: Call pygame.key.get_pressed() and use four if checks on the arrow keys to adjust x and y.

# Step 6: Clamp x and y with min() and max() so the sprite stays fully inside the screen.

# Step 7: Use an if/elif chain on x and y to set current_color whenever the sprite touches an edge.

# Step 8: Fill the screen black, draw the sprite rectangle in current_color, flip the display, and tick the clock.


import pygame
pygame.init()
def main():
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Sprite Movement and Color Change")
    colors = {"red": pygame.Color("red"), 
              "orange": pygame.Color("orange"),
              "yellow": pygame.Color("yellow"),
              "blue": pygame.Color("blue")}
    current_color = colors["white"] = pygame.Color("white")
    x, y = 250, 250
    width, height = 50, 50
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 5
        if keys[pygame.K_RIGHT]:
            x += 5
        if keys[pygame.K_UP]:
            y -= 5
        if keys[pygame.K_DOWN]:
            y += 5
        x = max(0, min(x, screen_width - width))
        y = max(0, min(y, screen_height - height))
        if x == 0:
            current_color = colors["red"]
        elif x == screen_width - width:
            current_color = colors["blue"]
        elif y == 0:
            current_color = colors["orange"]
        elif y == screen_height - height:       
            current_color = colors["yellow"]
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, width, height))
        pygame.display.flip()
        pygame.time.Clock().tick(60)
if __name__ == "__main__":
    main()
    pygame.quit()


