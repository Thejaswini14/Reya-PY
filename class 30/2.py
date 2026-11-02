import pygame
pygame.init()
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Pygame Window")
image = pygame.image.load("/Users/teju/Downloads/cheerful-kawaii-girl-stockcake.png").convert_alpha()
image = pygame.transform.scale(image, (400, 300))
text = pygame.font.Font(None, 36).render("Hello, Pygame!", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
def game_loop():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0, 0, 0))
        screen.blit(image, image_rect)
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    game_loop()
