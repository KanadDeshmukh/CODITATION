
# taking inputs for row and column size of the board r and s
BOARD_COLS = int(input('Column size c:'))
BOARD_ROWS = int(input('Row size r:'))
pieces=int(input('No of pieces you want in a row p:'))

# Object named Board 
class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]   #2d array for every slot where user can drop its peice
        self.turns = 0 #counting the turns
        self.last_move = [-1, -1] # checking last moves using rows and cols

  
    def print_board(self):
        print("\n")
        #for better understanding of the user using numbering here
        for r in range(BOARD_COLS): #loopinga through every column
            print(f"  ({r+1}) ", end="") #what col this number is?
        print("\n")


        # Printing the slots for created columns
        for r in range(BOARD_ROWS):
            print('|', end="")
            for c in range(BOARD_COLS):
                print(f"  {self.board[r][c]}  |", end="")  #another bar(|) to separate the columns
            print("\n")

        print(f"{'-' * 42}\n")  #printing dashes(--) to saperate 
        
        
    def which_turn(self):
        players = ['r', 'y']  #players red and yellow
        return players[self.turns % 2] #Based on nuber of turns one has played
    
    def in_bounds(self, r, c):
        return (r >= 0 and r < BOARD_ROWS and c >= 0 and c < BOARD_COLS)  #this will return boolen

    def turn(self, column):
        # Search bottom up for an open slot
        for i in range(BOARD_ROWS-1, -1, -1):  #go to first row and then subtract
            if self.board[i][column] == ' ':  #checking if its blank
                self.board[i][column] = self.which_turn()
                self.last_move = [i, column]       #Saving last move

                self.turns += 1         #incrementing the turn
                return True

        return False        #else false 

    def check_winner(self):     #function to check the winner
        last_row = self.last_move[0]  #checking with instance veriable  
        last_col = self.last_move[1]  #second index
        last_letter = self.board[last_row][last_col]

        # when we say its a connect position it will check all the elements around it, that is checking all directions
        directions = [[[-1, 0], 0, True],   
                      [[1, 0], 0, True], 
                      [[0, -1], 0, True],   #checking downwards
                      [[0, 1], 0, True],    #checking left  
                      [[-1, -1], 0, True],  #checking right 
                      [[1, 1], 0, True],    #checking diognally 
                      [[-1, 1], 0, True],
                      [[1, -1], 0, True]]
        
        # Search outwards looking for matching pieces
        
        for a in range(pieces):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))  #saving current row and column
                c = last_col + (d[0][1] * (a+1))    #shifting pos based on previous position

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == last_letter:  
                    d[1] += 1       
                else:
                    # Stop searching in this direction
                    d[2] = False

        # Checking possible diorection and no of pieces to form in a row'
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= pieces-1):
                self.print_board()
                print(f"{last_letter} is the winner!")
                return last_letter          #last letter will be the winner 

        # Did not find any winners
        return False

def play():       #creating an instance of an object which is Board
    # Initialize the game board
    game = Board()

    game_over = False       
    while not game_over:
        game.print_board()  #this was created inside class object

        # Ask the user for input, but only accept valid number of turns
        valid_move = False
        while not valid_move:
            user_move = input(f"{game.which_turn()}'s Turn, What column do you want to put your piece? Column range: (1-{BOARD_COLS}): ") #asking the user(players) to pick a column
            #what if user inputs a letter which is invalid?
            try:
                valid_move = game.turn(int(user_move)-1)    
            except:
                print(f"Please enter a valid  number between 1 and {BOARD_COLS}")

        # End the game if there is a winner
        game_over = game.check_winner()
        
        # Tie position at the end f the game
        if not any(' ' in x for x in game.board):
            print("This game is a draw :(")
            return


if __name__ == '__main__':   #to execute play() function
    play()