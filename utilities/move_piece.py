from utilities.load_pieces import load_screen
from utilities.grid import grid
from utilities.grid import turn


def is_valid_piece(piece, wt, wtg):
    wtg_piece = grid[wt][wtg][0]

    if piece.split("_")[0] == wtg_piece.split("_")[0]:
        return False

    return True


def move_piece(moves, screen):
    global turn
    where_from = moves[-2]
    where_to = moves[-1]

    if where_from != where_to:

        wf = where_from[0]
        wfg = int(where_from[-1]) - 1

        piece = grid[wf][wfg][0]

        wt = where_to[0]
        wtg = int(where_to[-1]) - 1

        if is_valid_piece(piece, wt, wtg):
            if piece.split("_")[0] == turn:

                grid[wf][wfg][0] = where_from
                grid[wt][wtg][0] = piece

                load_screen(screen)

                if turn == "white":
                    turn = "black"

                else:
                    turn = "white"

                return True

    return False
