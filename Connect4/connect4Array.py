import os
import sys
from time import sleep

DEBUGARR = False
DEBUGWHILE = True
DEBUGCONNECT4CHECK = True

connect4 = False
Player= 1

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
def checkConnect4(gameBoard, currRowCol, currPlayer):
    print("in Connect 4 Check")

    #Horizontal Check
    print(f"Row {currRowCol[0]}")    

    rowToCheck = gameBoard[currRowCol[0]]

    print(f"Row {rowToCheck}")
    
    #Horizontal Check
    if(horizontalCheck(rowToCheck, currPlayer)):
        return True

    #Vertical Check
    colToCheck = []
    for i in gameBoard:
        colToCheck.append(i[currRowCol[1]])

    print(colToCheck)
    if(verticalCheck(colToCheck, currPlayer)):
        return True

    concurrent = 0                  #is reset after finished with the checks

def checkEdge(gameboard, currRowCol):
    if (currRowCol[0] == 0 or currRowCol[1] == 0 or currRowCol[0] == (len(gameBoard)-1) or currRowCol[1] == (len(gameBoard[0])-1)):
        print("Edge")
        return True
    return False

def horizontalCheck(rowToCheck, currPlayer):
    concurrent = 0

    for i in rowToCheck:
        if (i == currPlayer):       #Used to iterate the concurrent value used to check for connect 4
            concurrent += 1

        elif (i != currPlayer):     #Used to reset the concurrent value used to check for connect 4
            concurrent = 0
        
        if (concurrent == 4):       #If Connect 4 happens
                print("Connect 4!!!!")
                return True
    
    return False

def verticalCheck(colToCheck, currPlayer):
    print("in Vertical Check")

    concurrent = 0

    for i in colToCheck:
        if (i == currPlayer):       #Used to iterate the concurrent value used to check for connect 4
            concurrent += 1

        elif (i != currPlayer):     #Used to reset the concurrent value used to check for connect 4
            concurrent = 0
        
        if (concurrent == 4):       #If Connect 4 happens
                print("Connect 4!!!!")
                return True

def diagonalCheck():
    print("in Diagonal Check")

#################################################################################################
#Checks for the checkConnect4 function
# def checkConnect4(gameBoard):
#     testArr1 = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,1,1,1,0]]

#     checkConnect4(gameBoard, enteredRowCol, Player)

# checkConnect4(gameBoard)

#################################################################################################
#Game main while

while (True and not connect4 and not isFullyPopulated(gameBoard)):

    os.system('cls' if os.name == 'nt' else 'clear')#Clears the terminal

    PlayerFinished = [False,-1,-1] #used to make sure that the Playeris finished

    for i in gameBoard:#prints the board
        print(i)
    
    try:
        choice = int(input(f"player: {Player}, what column?"))#gets the choice
        if(choice < 7 and choice >= 0):#if choice is valid, then runs insertPiece function
            PlayerFinished = insertPiece(Player, choice, gameBoard)
    except ValueError:
        sleep(0)
    except KeyboardInterrupt:
        sys.exit(1)

    enteredRowCol = [PlayerFinished[1],PlayerFinished[2]]#gets row and column that was just used, and stores in the format [row, column]

    if(DEBUGWHILE):
        print(enteredRowCol)
        print(PlayerFinished)
        print(checkEdge(gameBoard, enteredRowCol))
        

    connect4 = checkConnect4(gameBoard, enteredRowCol, Player)
    sleep(2)

    if(connect4):
        sleep(10)

    if(PlayerFinished[0]):#if the Playeris finished it changes the player, else, does nothing
        if(Player== 1):
            Player= 2
        else:
            Player= 1

#################################################################################################
#Game End
os.system('cls' if os.name == 'nt' else 'clear')#Clears the terminal

print("Final Board")
for i in gameBoard:#prints the board
        print(i)
