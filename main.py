from utilities.game import game


class Chess:
    def __init__(self):
        self.screen_size = (800, 800)
        self.square_size = min(self.screen_size[0], self.screen_size[1]) // 8

        self.color_schemes = {
            "white_and_gray": [(255, 255, 255), (192,192,192)],
            "chess.com": [(238, 238, 210), (118, 150, 86)],
        }
        self.current_scheme = self.color_schemes.get("chess.com")

        self.moves = []
        self.pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]

        self.is_a_move = False
        self.border_showing = True

    def main(self):
        game(
            self.screen_size,
            self.current_scheme,
            self.square_size,
            self.border_showing,
            self.moves,
            self.pieces,
        )


chess = Chess()
chess.main()
