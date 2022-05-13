import os
import sys
from time import sleep

DEBUGARR = False
DEBUGWHILE = True
DEBUGCONNECT4CHECK = True

connect4 = False
turn = 1

################################################################################################
#create Array
number_of_rows = 6
number_of_columns = 7
gameBoard=[]

for x in range(number_of_rows):
   column_elements=[]
   for y in range(number_of_columns):
       # Enter the all the values w.r.t to a particular column
       column_elements.append(0)
   #Append the column to the array.
   gameBoard.append(column_elements)

if (DEBUGARR):
    for i in gameBoard:
        print(i)

################################################################################################
#Methods for the game

#to insert Piece
def insertPiece(color, column, gameBoard):
    #this is to check the column and know where to put the number
    for i in range(0, len(gameBoard)):#goes through the rows
        if (gameBoard[(len(gameBoard)-1)-i][column] == 0):
            gameBoard[(len(gameBoard)-1)-i][column] = color
            return [True,(len(gameBoard)-1)-i,column]
    return [False,-1,-1]

#to check if fully populated array
def isFullyPopulated(gameBoard):
    for i in range(0,len(gameBoard)):
        for g in range(0,len(gameBoard[i])):
            if(gameBoard[i][g] == 0):
                return False
    return True

#to check if there is a connect 4
def checkConnect4(gameBoard, currRowCol):
    print("in Connect 4 Check")

    
def checkEdge(gameboard, currRowCol):
    if (currRowCol[0] == 0 or currRowCol[1] == 0 or currRowCol[0] == (len(gameBoard)-1) or currRowCol[1] == (len(gameBoard[0])-1)):
        print("Edge")
        return True
    return False

#################################################################################################
#Game main while

while (True and not connect4 and not isFullyPopulated(gameBoard)):

    os.system('cls' if os.name == 'nt' else 'clear')#Clears the terminal

    turnFinished = [False,-1,-1] #used to make sure that the turn is finished

    for i in gameBoard:#prints the board
        print(i)
    
    try:
        choice = int(input(f"player {turn}:, what column?"))#gets the choice
        if(choice < 7 and choice >= 0):#if choice is valid, then runs insertPiece function
            turnFinished = insertPiece(turn, choice, gameBoard)
    except ValueError:
        sleep(0)
    except KeyboardInterrupt:
        sys.exit(1)

    enteredRowCol = [turnFinished[1],turnFinished[2]]#gets row and column that was just used, and stores in the format [row, column]

    if(DEBUGWHILE):
        print(enteredRowCol)
        print(turnFinished)
        print(checkEdge(gameBoard, enteredRowCol))
        sleep(1)

    connect4 = checkConnect4(gameBoard, enteredRowCol)

    if(turnFinished[0]):#if the turn is finished it changes the player, else, does nothing
        if(turn == 1):
            turn = 2
        else:
            turn = 1

#################################################################################################
#Game End
os.system('cls' if os.name == 'nt' else 'clear')#Clears the terminal

print("Final Board")
for i in gameBoard:#prints the board
        print(i)
