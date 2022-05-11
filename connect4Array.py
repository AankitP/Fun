import os

DEBUGARR = False

connect4 = False
turn = 1

################################################################################################
#create Array
number_of_rows = 6
number_of_columns = 7
arr_2d=[]

for x in range(number_of_rows):
   column_elements=[]
   for y in range(number_of_columns):
       # Enter the all the values w.r.t to a particular column
       column_elements.append(0)
   #Append the column to the array.
   arr_2d.append(column_elements)

if (DEBUGARR):
    for i in arr_2d:
        print(i)

################################################################################################
#Methods for the game

#to insert token
def insertToken(color, column, arr_2d):
    #this is to check the column and know where to put the number
    for i in range(0, len(arr_2d)):#goes through the rows
        if (arr_2d[(len(arr_2d)-1)-i][column] == 0):
            arr_2d[(len(arr_2d)-1)-i][column] = color
            return True
    return False

#to check if fully populated array
def isFullyPopulated(arr_2d):
    for i in range(0,len(arr_2d)):
        for g in range(0,len(arr_2d[i])):
            if(arr_2d[i][g] == 0):
                return False
    return True

while (True and not connect4 and not isFullyPopulated(arr_2d)):

    os.system('cls' if os.name == 'nt' else 'clear')#Clears the terminal

    turnFinished = False #used to make sure that the turn is finished

    for i in arr_2d:#prints the board
        print(i)
    
    choice = int(input(f"player: {turn}, what column?"))#gets the choice
    
    if(choice < 7 and choice >= 0):#if choice is valid, then runs insertToken function
        turnFinished = insertToken(turn, choice, arr_2d)

    if(turnFinished):#if the turn is finished it changes the player, else, does nothing
        if(turn == 1):
            turn = 2
        else:
            turn = 1

#################################################################################################
#Game End
os.system('cls' if os.name == 'nt' else 'clear')#Clears the terminal

print("Final Board")
for i in arr_2d:#prints the board
        print(i)
