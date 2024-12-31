import pygame
from setting import *
from sys import exit

class GamePy():
    def __init__(self):
        self.list = []
        self.over = False
        
        pygame.init()
        self.font = pygame.font.Font(None, 74)
        window_size = SIZE
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Connect 4")

        self.create_game()

    def create_game(self):
        for i in range(GHIGHT+1):
            self.row = []
            if i == 0:
                for k in range(GWIDTH):
                    self.row.append(f'{k+1}')
            else:
                for _ in range(GWIDTH):
                    self.row.append(' ')
            self.list.append(self.row)

    def draw_grid(self):
        for x in range(0, SIZE[0], CELL_SIZE):
            pygame.draw.line(self.screen, 'grey', (x,0),(x,SIZE[1]))
        for y in range(0, SIZE[1], CELL_SIZE):
            pygame.draw.line(self.screen, 'grey', (0,y),(SIZE[0],y))

    def draw_board(self):
        for k in range(GWIDTH):
            self.draw_text(f'{k+1}', self.font, 'white', self.screen, k*CELL_SIZE, 0)

        for row in range(GHIGHT+1):
            for col in range(GWIDTH):
                if self.list[row][col] == 'x':
                    pygame.draw.circle(self.screen, 'red', center=(col*CELL_SIZE+CELL_SIZE//2, row*CELL_SIZE+CELL_SIZE//2) , radius=CELL_SIZE // 3)
                elif self.list[row][col] == 'o':
                    pygame.draw.circle(self.screen, 'blue', center=(col*CELL_SIZE+CELL_SIZE//2, row*CELL_SIZE+CELL_SIZE//2) , radius=CELL_SIZE // 3)
            
        
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj,textrect)

    def drop_piece(self, ind, xpos, piece):
        game.list[ind][xpos] = piece
        
    def player_won(self, player):
        self.player = player
        print(f' Player {self.player} won! ')
        self.quit_game()

    def quit_game(self):
        self.over = True
        pygame.quit()
        exit()

game = GamePy()
player = None
piece = None
turn = 0

while not game.over:
    if (turn % 2 == 0):
        player = '1'
        piece = 'x'
    else:
        player = '2'
        piece = 'o'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left mousebutton
                xpos = event.pos[0] // CELL_SIZE
                try:
                    for ind in range(GHIGHT+1):
                        if game.list[ind][xpos] != ' ':
                            ind += 1 
                        elif game.list[ind][xpos] == ' ':
                            game.drop_piece(ind, xpos, piece)
                            turn += 1
                            break
                    if event.pos[0] > GWIDTH * CELL_SIZE:
                        raise IndexError
                    break
                except IndexError:
                    print("Invalid column number:", event.pos[0] // CELL_SIZE)
                    print("Please try again.")
       
    game.screen.fill('black')
    game.draw_grid()
    game.draw_board()
    game.draw_text(f'Player {player} turn', game.font, 'white', game.screen, x=CELL_SIZE*9, y=CELL_SIZE)
    pygame.display.flip()

game.quit_game()