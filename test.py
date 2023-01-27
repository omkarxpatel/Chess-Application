import pygame

TILESIZE = 32
BOARD_POS = (10, 10)

def create_board_surf():
    board_surf = pygame.Surface((TILESIZE*8, TILESIZE*8))
    dark = False
    for y in range(8):
        for x in range(8):
            rect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(board_surf, pygame.Color('darkgrey' if dark else 'beige'), rect)
            dark = not dark
        dark = not dark
    return board_surf

def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - BOARD_POS
    x, y = [int(v // TILESIZE) for v in mouse_pos]
    try: 
        if x >= 0 and y >= 0: return (board[y][x], x, y)
    except IndexError: pass
    return None, None, None

def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)

    for x in range(0, 8):
        board[1][x] = ('black', 'pawn')
    for x in range(0, 8):
        board[6][x] = ('white', 'pawn') 

    return board

def draw_pieces(screen, board, font, selected_piece):
    sx, sy = None, None
    if selected_piece:
        piece, sx, sy = selected_piece

    for y in range(8):
        for x in range(8): 
            piece = board[y][x]
            if piece:
                selected = x == sx and y == sy
                color, type = piece
                s1 = font.render(type[0], True, pygame.Color('red' if selected else color))
                s2 = font.render(type[0], True, pygame.Color('darkgrey'))
                pos = pygame.Rect(BOARD_POS[0] + x * TILESIZE+1, BOARD_POS[1] + y * TILESIZE + 1, TILESIZE, TILESIZE)
                screen.blit(s2, s2.get_rect(center=pos.center).move(1, 1))
                screen.blit(s1, s1.get_rect(center=pos.center))

def draw_selector(screen, piece, x, y):
    if piece != None:
        rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)

def draw_drag(screen, board, selected_piece, font):
    if selected_piece:
        piece, x, y = get_square_under_mouse(board)
        if x != None:
            rect = (BOARD_POS[0] + x * TILESIZE, BOARD_POS[1] + y * TILESIZE, TILESIZE, TILESIZE)
            pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)

        color, type = selected_piece[0]
        s1 = font.render(type[0], True, pygame.Color(color))
        s2 = font.render(type[0], True, pygame.Color('darkgrey'))
        pos = pygame.Vector2(pygame.mouse.get_pos())
        screen.blit(s2, s2.get_rect(center=pos + (1, 1)))
        screen.blit(s1, s1.get_rect(center=pos))
        selected_rect = pygame.Rect(BOARD_POS[0] + selected_piece[1] * TILESIZE, BOARD_POS[1] + selected_piece[2] * TILESIZE, TILESIZE, TILESIZE)
        pygame.draw.line(screen, pygame.Color('red'), selected_rect.center, pos)
        return (x, y)

def main():
    pygame.init()
    font = pygame.font.SysFont('', 32)
    screen = pygame.display.set_mode((640, 480))
    board = create_board()
    board_surf = create_board_surf()
    clock = pygame.time.Clock()
    selected_piece = None
    drop_pos = None
    while True:
        piece, x, y = get_square_under_mouse(board)
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == pygame.MOUSEBUTTONDOWN:
                if piece != None:
                    selected_piece = piece, x, y
            if e.type == pygame.MOUSEBUTTONUP:
                if drop_pos:
                    piece, old_x, old_y = selected_piece
                    board[old_y][old_x] = 0
                    new_x, new_y = drop_pos
                    board[new_y][new_x] = piece
                selected_piece = None
                drop_pos = None

        screen.fill(pygame.Color('grey'))
        screen.blit(board_surf, BOARD_POS)
        draw_pieces(screen, board, font, selected_piece)
        draw_selector(screen, piece, x, y)
        drop_pos = draw_drag(screen, board, selected_piece, font)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()