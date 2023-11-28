import pygame
import main

pygame.init()
# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# setup pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("English to Pig Latin Translator")

base_font = pygame.font.Font(None, 18)
input_text = ""
output_text = ""
active = False

# create input text box
input_rect = pygame.Rect(200, 200, 200, 32)
active_color = pygame.Color(255, 255, 255)
inactive_color = pygame.Color('gray15')
input_color = inactive_color

# create output text box
output_rect = pygame.Rect(200, 250, 200, 32)
output_color = inactive_color

# create a translate button
translate_button = pygame.Rect(200, 300, 140, 50)
button_color = pygame.Color('pink')
button_text = "Translate"


run = True


def translate_to_pig_latin(text):
    translated_text = ""
    for word in text.split(" "):
        if not word.strip():
            continue
        translated_text += main.to_pig_latin(word) + " "
    return translated_text.strip()


# game loop
while run:
    screen.fill((255, 102, 153))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # activate input text if user clicks on text box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                input_color = active_color
            elif translate_button.collidepoint(event.pos):
                output_text = translate_to_pig_latin(input_text)
            # deactivate text box if user clicks off of it
            else:
                active = False
                input_color = inactive_color

        # register text to input text box
        if event.type == pygame.KEYDOWN and active == True:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                output_text = translate_to_pig_latin(input_text)
            elif event.key in (pygame.K_ESCAPE, pygame.K_TAB):
                active = False
                input_color = inactive_color
            else:
                input_text += event.unicode

    # Clear the screen
    screen.fill((255, 102, 153))

    # draw text boxes
    pygame.draw.rect(screen, input_color, input_rect, 2)
    pygame.draw.rect(screen, inactive_color, output_rect, 2)

    # draw button
    pygame.draw.rect(screen, button_color, translate_button)
    button_font = pygame.font.Font(None, 18)
    button_surface = button_font.render(button_text, True, (0, 0, 0))
    text_width, text_height = button_surface.get_size()
    screen.blit(button_surface, (translate_button.x + (translate_button.width -
                text_width) // 2, translate_button.y + (translate_button.height - text_height) // 2))

    # Render input text inside input rect
    text_surface = base_font.render(input_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(200, text_surface.get_width() + 10)

    # Render output text in output text box
    text_surface = base_font.render(output_text, True, (255, 255, 255))
    screen.blit(text_surface, (output_rect.x + 5, output_rect.y + 5))
    output_rect.w = max(200, text_surface.get_width() + 10)

    pygame.display.flip()

pygame.quit()
