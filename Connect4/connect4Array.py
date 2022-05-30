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

#The following functions are to check if there is a connect 4
def checkConnect4(gameBoard, currRowCol, currPlayer):   #Basic Method that is called when checking for connect 4
    print("in Connect 4 Check")

    for i in gameBoard:#prints the board
        print(i)

    print("\n\n")

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

    #Diagonal Check
        #The way this diagonal check will work is the same as the previous 2 checks
            #it will create an array of the diagonal that contains the position of the last
            #move played, and run the same check as the rest of the checks, will have a better
            #organized set of methods for this, because there is a great deal of code copy 
            #pasting.
    rightSideDiagonal = []
    leftSideDiagonal = []

    col = 0
    row = 0

    #Make the right diagonal 
    if(currRowCol[0] <= currRowCol[1]):
        col = currRowCol[1] - currRowCol[0]
        
    else:
        row = currRowCol[0] - currRowCol[1]


    while(row < 6 and col < 7):
        rightSideDiagonal.append(gameBoard[row][col])
        row += 1
        col += 1


    diagonalsToCheck = [rightSideDiagonal, leftSideDiagonal]

    if(diagonalsCheck(diagonalsToCheck, currPlayer)):
        return True

    concurrent = 0                                      #is reset after finished with the checks

def checkEdge(gameboard, currRowCol):                   #Checks if an edge piece (will be used later when attemptint to optimize)
    if (currRowCol[0] == 0 or currRowCol[1] == 0 or currRowCol[0] == (len(gameBoard)-1) or currRowCol[1] == (len(gameBoard[0])-1)):
        print("Edge")
        return True
    return False

def horizontalCheck(rowToCheck, currPlayer):            #This is to check if there is a horizontal connect 4 after a turn
    concurrent = 0

    for i in rowToCheck:
        if (i == currPlayer):                   #Used to iterate the concurrent value used to check for connect 4
            concurrent += 1

        elif (i != currPlayer):                 #Used to reset the concurrent value used to check for connect 4
            concurrent = 0
        
        if (concurrent == 4):                   #If Connect 4 happens
                print("Connect 4!!!!")
                return True
    
    return False

def verticalCheck(colToCheck, currPlayer):              #This is to check if there is a vertical connect 4 after a turn
    print("in Vertical Check")

    concurrent = 0

    for i in colToCheck:
        if (i == currPlayer):                   #Used to iterate the concurrent value used to check for connect 4
            concurrent += 1

        elif (i != currPlayer):                 #Used to reset the concurrent value used to check for connect 4
            concurrent = 0
        
        if (concurrent == 4):                   #If Connect 4 happens
                print("Connect 4!!!!")
                return True

    return False

def diagonalsCheck(diagonalToCheck, currPlayer):         #This is to check if there is a Diagonal connect 4 after a turn
    print("in Diagonal Check")

    

    return False

#################################################################################################
# Checks for the checkConnect4 function
def checkConnect4Wins(gameBoard):
    testArr1 = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,1,1,1,1,1]]
    testArr2 = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,2,1,0,0],[0,0,0,2,2,1,0],[0,0,0,2,2,2,1]]
    testArr3 = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,1,2,0,0,0],[0,1,2,2,0,0,0],[1,2,2,2,0,0,0]]

    print(checkConnect4(testArr2, [2,3], 1))
    print(checkConnect4(testArr3, [2,3], 1))

checkConnect4Wins(gameBoard)

#################################################################################################
#Game main while

# while (True and not connect4 and not isFullyPopulated(gameBoard)):

#     os.system('cls' if os.name == 'nt' else 'clear')#Clears the terminal

#     PlayerFinished = [False,-1,-1] #used to make sure that the Playeris finished

#     for i in gameBoard:#prints the board
#         print(i)
    
#     try:
#         choice = int(input(f"player: {Player}, what column?"))#gets the choice
#         if(choice < 7 and choice >= 0):#if choice is valid, then runs insertPiece function
#             PlayerFinished = insertPiece(Player, choice, gameBoard)
#     except ValueError:
#         sleep(0)
#     except KeyboardInterrupt:
#         sys.exit(1)

#     enteredRowCol = [PlayerFinished[1],PlayerFinished[2]]#gets row and column that was just used, and stores in the format [row, column]

#     if(DEBUGWHILE):
#         print(enteredRowCol)
#         print(PlayerFinished)
#         print(checkEdge(gameBoard, enteredRowCol))
        

#     connect4 = checkConnect4(gameBoard, enteredRowCol, Player)
#     sleep(2)

#     if(connect4):
#         sleep(10)

#     if(PlayerFinished[0]):#if the Playeris finished it changes the player, else, does nothing
#         if(Player== 1):
#             Player= 2
#         else:
#             Player= 1

# #################################################################################################
# #Game End
# os.system('cls' if os.name == 'nt' else 'clear')#Clears the terminal

# print("Final Board")
# for i in gameBoard:#prints the board
#         print(i)
