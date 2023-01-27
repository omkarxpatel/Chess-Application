import pygame
from utilities.grid import grid


def is_valid(item):
    if item in ["pawn", "knight", "bishop", "rook", "queen", "king"]:
        return True

    return False


def load_screen(screen):
    columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for col in columns:
        row = grid.get(col)

        for item in row:

            valid_check = item[0].split("_")[-1]
            if is_valid(valid_check):

                image = pygame.image.load(f"assets/images/imgs-80px/{item[0]}.png")
                screen.blit(image, item[-1])
