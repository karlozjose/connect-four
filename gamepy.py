""" Connect 4 using PyGame graphics"""

import pygame
from setting import *
from sys import exit

class GamePy():
    def __init__(self):
        self.list = []
        self.over = False
        
        pygame.init()
        self.font = pygame.font.Font(None, 60)
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
        for x in range(0, (GWIDTH + 1) * CELL_SIZE, CELL_SIZE):
            pygame.draw.line(self.screen, 'grey', (x,0),(x,(GHIGHT + 1) * CELL_SIZE))
        for y in range(0, (GHIGHT + 2) * CELL_SIZE, CELL_SIZE):
            pygame.draw.line(self.screen, 'grey', (0,y),(GWIDTH * CELL_SIZE,y))

    def draw_board(self):
        for k in range(GWIDTH):
            self.draw_text(f'{k+1}', self.font, 'white', self.screen, k*CELL_SIZE + GRID_SIZE // 2, 1)

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
    
    def draw_square(self): # draws the background of the words on the side
        pygame.draw.rect(self.screen, color='white', rect=(CELL_SIZE*8 - 5, CELL_SIZE - 5, CELL_SIZE*8 + 10, CELL_SIZE*3 + 10), border_radius=6)
        pygame.draw.rect(self.screen, color='grey', rect=(CELL_SIZE*8, CELL_SIZE, CELL_SIZE*8, CELL_SIZE*3), border_radius=6)

    def drop_piece(self, ind, xpos, piece):
        self.list[ind][xpos] = piece
        
    def player_won(self, player, color):
        print(f' Player {player} won! ')
        self.screen_update()
        self.draw_text(f'Player {player} won!', self.font, color, self.screen, x=CELL_SIZE*9, y=CELL_SIZE*2)
        pygame.display.flip()
        pygame.time.wait(2000)
        self.quit_game()

    def screen_update(self):
        self.screen.fill('black')
        self.draw_grid()
        self.draw_board()
        self.draw_square()

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
        color = 'red'
    else:
        player = '2'
        piece = 'o'
        color = 'blue'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left mousebutton
                xpos = event.pos[0] // CELL_SIZE
                try:
                    for ind in range(GHIGHT, 0, -1):
                        if game.list[ind][xpos] != ' ':
                            continue 
                        elif game.list[ind][xpos] == ' ':
                            game.drop_piece(ind, xpos, piece)
                            turn += 1
                            break
                    if event.pos[0] > GWIDTH * CELL_SIZE:
                        raise IndexError
                    break
                except IndexError:
                    print("Invalid column number:", event.pos[0] // CELL_SIZE + 1)
                    print("Please try again.")

    # check for winning game
    for k in range(GHIGHT, 0, -1): # range(1, GHIGHT + 1)
        for j in range(GWIDTH):
            if game.list[k][j] != ' ':
                if 0 <= j < GWIDTH-3:
                    if game.list[k][j] == game.list[k][j+1] == game.list[k][j+2] == game.list[k][j+3]:
                        game.player_won(player, color)
                    
                if 0 <= k <= GHIGHT-3:
                    if game.list[k][j] == game.list[k+1][j] == game.list[k+2][j] == game.list[k+3][j]:
                        game.player_won(player, color)

                if (0 <= j < GWIDTH-3) & (0 <= k <= GHIGHT-3):
                    if game.list[k][j] == game.list[k+1][j+1] == game.list[k+2][j+2] == game.list[k+3][j+3]:
                        game.player_won(player, color)

                if (3 <= j < GWIDTH) & (0 <= k <= GHIGHT-3):
                    if game.list[k][j] == game.list[k+1][j-1] == game.list[k+2][j-2] == game.list[k+3][j-3]:
                        game.player_won(player, color)

    game.screen_update()
    game.draw_text(f'Player {player} turn', game.font, color, game.screen, x=CELL_SIZE*9, y=CELL_SIZE*2)
    pygame.display.flip()

    if ' ' not in game.list[1]:
        game.screen_update()
        game.draw_text(f'It\'s a tie!', game.font, 'white', game.screen, x=CELL_SIZE*9, y=CELL_SIZE*2)
        pygame.display.flip()
        print('No more moves available. Thank you for playing!')
        pygame.time.wait(2000)
        game.quit_game()


game.quit_game()