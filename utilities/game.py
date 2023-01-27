import pygame
from utilities.grid import grid
from utilities.move_piece import move_piece
from utilities.create_board import create_board


def get_square(position, square_size):
    values = ["a", "b", "c", "d", "e", "f", "g", "h"]
    values_num = [1, 2, 3, 4, 5, 6, 7, 8][::-1]

    x, y = position
    row = y // square_size
    col = x // square_size
    square = (col, row)

    # print(f"Mouse is over square: {square}, {values[col]}{values_num[row]}")
    return f"{values[col]}{values_num[row]}"


def add_border(coord, screen, border_showing):
    if border_showing:

        red_border = pygame.image.load(f"assets/images/imgs-100px/red_border.png")

        screen.blit(red_border, coord)
        pygame.display.flip()


def game(screen_size, current_scheme, square_size, border_showing, moves, pieces):

    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Chessboard")

    playing = True
    while playing:

        try:
            create_board(current_scheme, screen, square_size)

        except pygame.error:
            print(pygame.error)
            playing = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                pos = pygame.mouse.get_pos()
                square = get_square(pos, square_size)

                wf = square[0]
                wfg = int(square[-1]) - 1

                piece = grid[wf][wfg][0]
                piece = piece.split("_")[-1]

                coord = grid[wf][wfg][-1]

                new_coord = (coord[0] - 10, coord[-1] - 5)
                add_border(new_coord, screen, border_showing)
                border_showing = True

                if piece in pieces:
                    moves.append(square)

                else:
                    if len(moves) > 0:
                        bf = moves[-1][0]
                        bfg = int(moves[-1][-1]) - 1

                        piece = grid[bf][bfg][0]
                        piece = piece.split("_")[-1]

                        if piece in pieces:
                            moves.append(square)

                if len(moves) >= 2:

                    if move_piece(moves, screen):
                        is_a_move = False

                    else:
                        is_a_move = True

    pygame.quit()
