import pygame
import main

pygame.init()
# screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

# setup pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("English to Pig Latin Translator")

base_font = pygame.font.Font(None, 18)
title_font = pygame.font.Font(None, 36)
header_font = pygame.font.Font(None, 24)

title_text = "English to Pig Latin Translator"
input_text = ""
output_text = ""
active = False

# create input text box
text_box_width = 400
text_box_x = (SCREEN_WIDTH - text_box_width) // 2
input_text_box_y = 150
input_rect = pygame.Rect(text_box_x, input_text_box_y, text_box_width, 32)
active_color = pygame.Color(255, 255, 255)
inactive_color = pygame.Color('gray15')
input_color = inactive_color

# create output text box
output_text_box_y = 250
output_rect = pygame.Rect(text_box_x, output_text_box_y, text_box_width, 32)
output_color = inactive_color

# create a translate button
button_width = 140
button_x = (SCREEN_WIDTH - button_width) // 2
translate_button = pygame.Rect(button_x, 325, button_width, 50)
button_color = pygame.Color('pink')
button_text = "Translate"


run = True


def translate(text):
    """
    translate parses some text and translates each word to pig latin and then concatenates the translation back together

    :param text: the text to be translated to pig latin
    :return: the pig latin translation of the text that was passed
    """
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
                output_text = translate(input_text)
            # deactivate text box if user clicks off of it
            else:
                active = False
                input_color = inactive_color

        # register text to text box
        if event.type == pygame.KEYDOWN and active == True:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                output_text = translate(input_text)
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
    button_surface = base_font.render(button_text, True, (0, 0, 0))
    text_width, text_height = button_surface.get_size()
    screen.blit(button_surface, (translate_button.x + (translate_button.width -
                text_width) // 2, translate_button.y + (translate_button.height - text_height) // 2))

    # Render Title
    title_surface = title_font.render(title_text, True, (255, 255, 230))
    title_width, title_height = title_surface.get_size()
    screen.blit(title_surface, ((SCREEN_WIDTH - title_width) // 2, 50))

    # Render Headers
    header1_surface = header_font.render(
        "Enter some english here:", True, (255, 255, 230))
    header1_width, header1_height = header1_surface.get_size()
    screen.blit(header1_surface, (text_box_x + 10, input_text_box_y - 25))

    header2_surface = header_font.render(
        "Translated text:", True, (255, 255, 230))
    header2_width, header2_height = header2_surface.get_size()
    screen.blit(header2_surface, (text_box_x + 10, output_text_box_y - 25))

    # Render text to text boxes
    input_surface = base_font.render(input_text, True, (255, 255, 255))
    screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = max(400, input_surface.get_width() + 10)

    output_surface = base_font.render(output_text, True, (255, 255, 255))
    screen.blit(output_surface, (output_rect.x + 5, output_rect.y + 5))
    output_rect.w = max(400, output_surface.get_width() + 10)

    # only rerender the text boxes on next iteration
    pygame.display.update([input_rect, output_rect])

    pygame.display.flip()

pygame.font.quit()
pygame.quit()
