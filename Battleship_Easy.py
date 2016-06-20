from random import randint  # randint generates a random interger in the range provided

board = [] # initializes an empty board so that spaces can be appended to it later

for x in range(3):
    board.append(["O"] * 3) # inserts three rows of ["O","O","O"] into the board 

def print_board(board): 
    for row in board:
        print (" ".join(row)) # prints the board row by row in a legible format

def random_row(board):
    return randint(0, len(board) - 1) # generates a random number corresponding to an index of a row of the board

def random_col(board):
    return randint(0, len(board[0]) - 1) # generates a random number corresponding to an index of a col of the board

# main    
print("Let's play Battleship!")
print_board(board) 

for turn in range(4):
    ship_row = random_row(board) # places the ship
    ship_col = random_col(board) # places the ship
    guess_row = int(input("Guess Row:"))-1 # gets row from user and converts to index. input must be a number
    guess_col = int(input("Guess Col:"))-1 # gets col from user and converts to index. input must be a number
    # check hit
    if guess_row == ship_row and guess_col == ship_col: # if the user has hit the shio
        print ("Congratulations! You sunk the battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 3) or (guess_col < 0 or guess_col > 3): # out of range
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"): # the spot has already been hit
            print("You guessed that one already.")
        else: # the player hits an empty spot
            print("You missed the battleship!")
            board[guess_row][guess_col] = "X" 
        if turn==3: # after four turns
            print("Game Over")
            print("The Battleship is in row", ship_row, ", col", ship_col)
            
    print("Turn", turn+1)
    print_board(board)
