# This code could be made a LOT more efficient but I started writing with dictionaries and then switched to lists in order to experiment
# We use a dictionary with list + sublist with index rows[row #] = [# x, # o], columns[column #] = [#x, #o], diagonal[1 or 2] = [#x, #o]

# Global variables
boardSize = 5
rows = [[0,0] for a in range(0, boardSize)]
columns = [[0,0] for a in range(0, boardSize)]
diagonals = [[0,0],[0,0]]

def convertToArray(cell):
    row = (cell - 1) // boardSize                               # Floored division, gives how many times it fits into the number
    column = (cell - 1) % boardSize                             # Gives remainder
    diagonal = 2

    if row == column:
        diagonal = 0                                            # Diagonal 0 is \, diagonal 1 is /
    elif (row+column) == (boardSize-1):
        diagonal = 1

    return (row, column, diagonal)

def displayBoard(board):
    lineString = ""

    for j in range(boardSize):
        for i in range(boardSize):
            lineString += (board[i + 1 + j*boardSize] + "  ")
        print(lineString)
        lineString = ""

def checkIfLegal(number, occupiedTiles):
    state = None
    errorCode = None
    if number > 25 or number < 1:
        state = False
        errorCode = 1
    if number in occupiedTiles:
        state = False
        errorCode = 2
    elif number not in occupiedTiles and number < 26 and number > 0:
        state = True 
    return state, errorCode

def checkWinner(board):
    winState = None
    return winState # Completely not finished lol

#def computerMove(board):
    #a

#def smartComputerMove(board):
    #s

def main():
    board = dict([(a, f"{a:02.0f}") for a in range(1, boardSize**2+1)])                 # For i in range, this creates a tuple with a key and value, adds it to a list which is then turned into a dictionary. The format string is used to create numbers "01", "02", and so on
    
    occupiedTiles = []
    print("Hello and welcome to the Tic-Tac-Toe Comp 208 challenge: Player against Computer.\nThe board is numbered from 1 to 25 as per the following:")
    displayBoard(board)
    print("Player starts first. Simply input the number of the cell you want to occupy. Player’s move is marked with X. Computer’s move is marked with O.")
    while True:
        userInput = input("Start? (y/n) ")
        if userInput == "y" or userInput == "Y":
            break
        elif userInput == "n" or userInput == "N":
            exit()
        else:
            print("Invalid input, try again.")
    
    while checkWinner(board) == None:
        while True:
            while True:
                try:
                    number = int(input("Which number of the board would you like to occupy? "))
                    break
                except ValueError:
                    print("Please enter an integer.")
            
            state, errorCode = checkIfLegal(number, occupiedTiles)
            
            if state == False:
                if errorCode == 1:
                    print("Number is out of bounds, try again.")
                if errorCode == 2:
                    print("Number is occupied already, try again.")
            elif state == True:
                print("Number is legal, adding to the board...")
                board[number] = "x "
                occupiedTiles.append(number)
                
                row, column, diagonal = convertToArray(number)
        
main() 