#Import from library
from random import randint
from random import shuffle

#Initialize board
board = #(an empty array)#

#Build board
for x in range(10):
    board.#(function to add to end of array)#(["O"] * 10)
    
#Place ships
randomrow = [0,1,2,3,4,5,6,7,8,9]
shuffle(randomrow)
ships=[["carrier",randint(0,5),randomrow[0],5,5],#(make four more ships, with the structure of ["NAME",COL,ROW,NUMBER OF PIECES,NUMBER OF PIECES])#]

#Print board
def print_board():
    #(loop through each row in the board)#
        print (" ".join(row))

#Get input
def get_row():
    return input("Guess Row:")
#(define a similar function to get the Col)#

#Check input
def check_input(row,col):
    try:
        row=int(row)-1
        col=int(col)-1
        if (row < 0 or row > 10) or #(Check if the Col is out of range)#:
            print ("Oops, that's not even in the ocean.")
            return False
        elif board[row][col] == "@" or board[row][col]=="X" or board[row][col]=="-":
            print (#(When will this occur?)#)
            return False
        return True
    except ValueError:
        return False

    
#Check for hit
def check_hit(row,col):
    hit=0
    for ship in ships:
        if (ship[1])<=col<=(ship[1]+ship[4]) and row==ship[2]:
            hit=1
            ship[3]-=1
            if ship[3]==0:
                print ("You sank the " + ship[0] + "!")
                for i in range(ship[4]):
                    board[ship[2]][ship[1]+i]="-"
            else:
                print("You hit a ship!")
                board[row][col]="X"
    if hit==0:
        print(#(When will this occur?)#)
        board[row][col]="@"

#Check for win
def check_win():
    #(loop through ships)#
        #(Check if there are any pieces of the ship left)#
            return False
    return True

#Main
print ("Let's play Battleship!")
print ("You have 30 turns to sink all the ships. \nSelect a row and column between 1 and 10 as a target. \nO denotes an unknown spot. @ denotes an empty spot. \nX denotes a hit. - denotes a sunken ship.")
print_board()
for turn in range(100):
    row=get_row()
    col=get_col()
    #(While the input is invalid, get the player to try entering coordinates again)#
    row=int(row)-1
    col=int(col)-1
    check_hit(row,col)
    #(If the user has won, print "You win" and exit loop)#
    print_board()
    #(If the player has exceeded to maximum amount of turns, exit the loop and print "Game over")#
    #(Tell the player what turn it is)#
