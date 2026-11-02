# Step 1: Import pygame and call pygame.init() to start it up.

# Step 2: Create a 400x400 display window using pygame.display.set_mode() and store it in window.

# Step 3: Fill the window with white using window.fill((255, 255, 255)).

# Step 4: Store the color green in a variable named GREEN.

# Step 5: Draw a solid circle with pygame.draw.circle(window, GREEN, (300, 300), 50).

# Step 6: Draw a hollow circle with pygame.draw.circle(window, GREEN, (100, 100), 50, 3), using width 3 for the outline.

# Step 7: Call pygame.display.update() to show both circles, then run an event loop that quits when the window closes.


import pygame
pygame.init()
window = pygame.display.set_mode((400, 400))
window.fill((255, 255, 255))
GREEN = (0, 255, 0)
pygame.draw.circle(window, GREEN, (300, 300), 50)
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)
pygame.display.update()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
