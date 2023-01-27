import pygame
from utilities.grid import grid
from utilities.move_piece import move_piece
from utilities.create_board import create_board

class Chess():
    def __init__(self):
        self.screen_size = (800,800)
        self.square_size = min(self.screen_size[0], self.screen_size[1]) // 8

        self.color_schemes = [
                                [(255,255,255), (0,0,0)],# White and Black
                                [(238,238,210), (118,150,86)] # Chess.com
                            ]
        self.current_scheme = 1
        self.moves = []

        self.playing = True
        self.is_a_move = False
        self.border_showing = True
        
        self.pieces = ["pawn","knight","bishop","rook","queen","king"]
        
        
    def get_square(self, position):
        values = ["a","b","c","d","e","f","g","h"]
        values_num = [1,2,3,4,5,6,7,8][::-1]
        
        x, y = position
        row = y // self.square_size
        col = x // self.square_size
        square = (col, row)
        
        
        # print(f"Mouse is over square: {square}, {values[col]}{values_num[row]}")
        return f"{values[col]}{values_num[row]}"
    
    def add_border(self, coord, screen):
        if self.border_showing:
                    
            red_border = pygame.image.load(f"assets/images/100x100-ff00007f.png")
        
            screen.blit(red_border, coord)
            pygame.display.flip()    
        
        
    def main(self):
        # initializing pygame and setting up the screen
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Chessboard")

        # game loop
        playing = True
        while playing:

            # creating the board
            try:
                create_board(self.color_schemes, self.current_scheme, screen, self.square_size)
                
            except pygame.error:
                print(pygame.error); playing = False
                
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    pos = pygame.mouse.get_pos()
                    square = self.get_square(pos)
                    
                    wf = square[0]
                    wfg = int(square[-1])-1
                    
                    piece = grid[wf][wfg][0]
                    piece = piece.split("_")[-1]
                    
                    coord = grid[wf][wfg][-1]
                    
                    new_coord = (coord[0]-10, coord[-1]-5)
                    self.add_border(new_coord, screen)
                    self.border_showing = True


                    if piece in self.pieces:
                        self.moves.append(square)
                    
                    else:
                        bf = self.moves[-1][0]
                        bfg = int(self.moves[-1][-1])-1
                        
                        piece = grid[bf][bfg][0]
                        piece = piece.split("_")[-1]
                        
                        if piece in self.pieces:
                            self.moves.append(square)
                            
                    
                    if len(self.moves) >= 2:
                                                    
                        if move_piece(self.moves, screen):
                            self.is_a_move = False
                            
                        else:
                            self.is_a_move = True
                    
                    
        pygame.quit()
            
            
            
chess = Chess()
chess.main()