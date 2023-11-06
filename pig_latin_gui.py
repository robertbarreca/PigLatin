import pygame

pygame.init()
# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# setup pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("English to Pig Latin Translator")

base_font = pygame.font.Font(None, 18)
input_text = ""

# create input text box
input_rect = pygame.Rect(200, 200, 140, 32)
color = pygame.Color(255, 255, 255)


run = True
# game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Clear the screen
    screen.fill((0, 0, 0))

    # draw text box
    pygame.draw.rect(screen, color, input_rect, 2)

    # Render input text inside input rect
    text_surface = base_font.render(input_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(200, text_surface.get_width() + 10)

    pygame.display.flip()

pygame.quit()
