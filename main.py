""" Creating a simple connect 4 """
"Will use lists"

from sys import exit

GWIDTH = 7
GHIGHT = 6 

class Game():
    def __init__(self):
        self.list = []
        self.over = False
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

    def print_board(self):
        for ind, row in enumerate(reversed(self.list)):
            print(len(self.list) - ind - 1, row)

    def player_won(self, player):
        self.player = player
        print(f' Player {self.player} won! ')
        self.over = True
        exit()

game = Game()
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
    
    game.print_board()

    while True: # this loop works to try/except infinite times until it is correct input
        try:
            player_input = int(input(f"Player {player} with piece '{piece}' enter a column number from 1-{GWIDTH}:  "))
            if player_input < 1 or player_input > GWIDTH:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print(f"Invalid integer. The number must be in the range of 1-{GWIDTH}. ")
        
    col = int(player_input) - 1 # compensate index starting with 0.

    # check if lowest row has an item or anythin in it. 
    for i in range(GHIGHT+1):
        if game.list[i][col] != ' ':
            i += 1
        elif game.list[i][col] == ' ':
            game.list[i][col] = piece
            break

    # check for winning game
    # use j and k 
    for k in range (GHIGHT):
        for j in range(GWIDTH):
            if game.list[k][j] != ' ':
                if 0 <= j < GWIDTH-3:
                    if game.list[k][j] == game.list[k][j+1] == game.list[k][j+2] == game.list[k][j+3]:
                        game.print_board()
                        game.player_won(player)
                       
                if 0 <= k < GHIGHT-3:
                    if game.list[k][j] == game.list[k+1][j] == game.list[k+2][j] == game.list[k+3][j]:
                        game.print_board()
                        game.player_won(player)

                if (0 <= j < GWIDTH-3) & (0 <= k < GHIGHT-3):
                    if game.list[k][j] == game.list[k+1][j+1] == game.list[k+2][j+2] == game.list[k+3][j+3]:
                        game.print_board()
                        game.player_won(player)

                    if game.list[k][j] == game.list[k+1][j-1] == game.list[k+2][j-2] == game.list[k+3][j-3]:
                        game.print_board()
                        game.player_won(player)
    turn += 1