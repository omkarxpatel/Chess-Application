import pygame
import pygame.font
from utilities.load_pieces import load_screen

def create_board(color_schemes, current_scheme, screen, square_size):
    # Create a font object
    font = pygame.font.Font(None, square_size // 3)

    # creating the grid
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 == 0:
                color = color_schemes[current_scheme][0]
            else:
                color = color_schemes[current_scheme][1]
            pygame.draw.rect(screen, color, (col*square_size, row*square_size, square_size, square_size))
            
            
            add_numbers_letters = False   
            
            if add_numbers_letters:
                add_letters(row, screen, font, col, square_size)
                add_numbers(row, screen, font, col, square_size)
                
                
    load_screen(screen)

    # updating the screen
    pygame.display.flip()

# adds the letters 
def add_letters(row, screen, font, col, square_size):
    if row == 0:
        letter = chr(ord('A') + col)
        text = font.render(letter, True, (255, 225, 0))
        screen.blit(text, ((col*square_size + square_size // 4), 50)) # (col*square_size + square_size // 4)
        
# adds the numbers
def add_numbers(row, screen, font, col, square_size):
    if col == 0:
        number = str(8 - row)
        text = font.render(number, True, (255, 225, 0))
        screen.blit(text, (0, row*square_size + square_size // 4))