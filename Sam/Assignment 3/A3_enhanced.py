# This code could be made a LOT more efficient but I started writing with dictionaries and then switched to lists in order to experiment
# We use a dictionary with list + sublist with index rows[row #] = [# x, # o], columns[column #] = [#x, #o], diagonal[1 or 2] = [#x, #o]
# This could have made simpler if I had known about sublists inside lists beforehand. But I took this as a challenge rather than rewriting the code

from random import randint

# Global variables that are to be kept outside of local variables in order to keep values between iterations
boardSize = 0                                                                                                   # Will be easier to do the enhanced version if we don't hardcode straight away
rows = []                                                                     # For each row, we create sublists as described in line 2. Same with columns
columns = []
diagonals = [[0,0],[0,0]]                                                                                       # Same as stated above, except these are hardcoded as there will always be two

centerTaken = False                                                                                             # Flag
cornersTaken = False                                                                                            # Flag

def convertToArray(cell):                                                                                       # It is simpler and more clean to have a single function for this
    row = (cell - 1) // boardSize                                                                               # Floored division, gives how many times it fits into the number
    column = (cell - 1) % boardSize                                                                             # Gives remainder to determine column
    diagonal = 3                                                                                                # Default value, basically means null as stated below

    if (row+column) == (boardSize-1) and row == column:                                                         # If number is in both diagonals, it's the center
        diagonal = 2
    elif row == column:                                                                                         # If i == j
        diagonal = 0                                                                                            # Diagonal 0 is \, diagonal 1 is /, center is 2, 3 = None
    elif (row+column) == (boardSize-1):                                                                         # If i + j == length of one side
        diagonal = 1
    else:
        diagonal = 3
    return (row, column, diagonal)                                                                              # "array"

def displayBoard(board):
    lineString = ""                                                                                             # Text we will display for each line

    for j in range(boardSize):                                                                                  # For every column in board
        for i in range(boardSize):                                                                              # For row in board 
            lineString += (board[i + 1 + j*boardSize] + "  ")                                                   # We concatenate all the cells in each row
        print(lineString)
        lineString = ""                                                                                         # Reset

def checkIfLegal(number, occupiedTiles):                                                                        # It is more efficient to check with a list of already occupied cells
    state = None                                                                                                # Legality of the move
    errorCode = None                                                                                            # We pass error codes to make it cleaner
    if number > boardSize**2 or number < 1:                                                                     # If out of bound error, return 1
        state = False
        errorCode = 1
    if number in occupiedTiles:                                                                                 # If number is already taken, return 2
        state = False
        errorCode = 2
    elif number not in occupiedTiles and number < (boardSize**2+1) and number > 0:                              # Otherwise, return state = True
        state = True 
    return state, errorCode

def checkWinner(updated, occupied, turn):
    row, col, diagonal = updated                                                                                # "updated" means the tuple from convertToArray that the player has updated by placing an x
                                                                                                                # Turn = 0 if player, 1 if computer
    if rows[row][turn] == boardSize or columns[col][turn] == boardSize:                                         # If we get a number of x or o equal to boardSize, we have a winner identified by the turn index
        if turn == 0:
            print("Player wins. Congratulations")
            exit()
        elif turn == 1:
            print("Computer wins.")
            exit()
    if diagonal in [0,1]:                                                                                       # We don't bother checking if diagonals aren't present (i.e. diagonal = 3)
        if diagonals[diagonal][turn] == boardSize:
            if turn == 0:
                print("Player wins. Congratulations")
                exit()
            elif turn == 1:
                print("Computer wins.")
                exit()
    if len(occupied) == boardSize**2:                                                                           # If all cells are occupied and there are no winners, it's a draw
        print("The game is a draw.")
        exit()

def appendCounters(number, turn):
    row, col, diagonal = convertToArray(number)
    rows[row][turn] += 1
    columns[col][turn] += 1
    if diagonal in [0,1]:
        diagonals[diagonal][turn] += 1
    elif diagonal == 2:
        diagonals[0][turn] += 1
        diagonals[1][turn] += 1

def computerMove(board, occupied):
    while True:                                                                                                 # Keep going until a number is found
        randomMove = randint(0,boardSize**2)                                                                    # This function excludes 0 but includes boardSize**2
        state = checkIfLegal(randomMove, occupied)[0]
        if state == True:
            break
    return randomMove

def smartComputerMove(board, occupied, playerMove, previousMove):                                               # Algorithm: check if a line can be blocked, check if a column can be blocked, 
    row, col, diagonal = playerMove                                                                             # check if a diagonal can be blocked, check if center is occupied, check if center 
    global centerTaken                                                                                          # is occupied, check if corners are occupied, check if sides are occupied
    global cornersTaken
    
    # This checks for any AI winning opportunities based on the previous move
    if previousMove != None:                                                                                    # This becomes available at turn 2, it checks for the AI's previous move
        rowAI, colAI, diagonalAI = convertToArray(previousMove)
        
        if (columns[colAI][1] == (boardSize - 1) ) and ( (columns[colAI][0]+columns[colAI][1]) < boardSize):    # We only bother checking if the row, column, or diagonal has 4 o
            for a in range(0, boardSize):                                                                       # We check for every column, row, or column
                b = colAI + 1 + a*boardSize                                                                     # This gives us the cell numbers within that row, column, or diagonal
                if checkIfLegal(b, occupied)[0] == True:                                                        # Then we check if it is legal
                    return b                                                                                    # If it is, we return the number and end the function. 
                                                                                                                # Rinse and repeat for the below statements
        if (rows[rowAI][1] == (boardSize - 1) ) and ( (rows[rowAI][0]+rows[rowAI][1]) < boardSize):
            for a in range(0, boardSize):
                b = rowAI*boardSize + 1 + a 
                if checkIfLegal(b, occupied)[0] == True:
                    return b

        if diagonalAI in [0,1]:                                                                                 # Only bother checking if the last updated number was in a diagonal, either 1 or 2
            if diagonals[0][1] == (boardSize-1) and ( (diagonals[0][0] + diagonals[0][1]) < boardSize):
                for a in range(0, boardSize):
                    b = 1 + a*(boardSize+1)
                    if checkIfLegal(b, occupied)[0] == True:
                        return b
            
            if diagonals[1][1] == (boardSize-1) and ( (diagonals[1][0] + diagonals[1][1]) < boardSize):
                for a in range(0, boardSize):
                    b = boardSize + a*(boardSize-1)
                    if checkIfLegal(b, occupied)[0] == True:
                        return b
    
    # This checks the player's move for potential winning opportunities. If it sees any, it prevents the player to the best of its ability.
    if (rows[row][0] == (boardSize - 1) ) and ( (rows[row][0]+rows[row][1]) < boardSize):                       # We only bother checking if the row, column, or diagonal has 4 x
        for a in range(0, boardSize):
            b = row*boardSize + 1 + a 
            if checkIfLegal(b, occupied)[0] == True:
                return b
    
    if (columns[col][0] == (boardSize - 1) ) and ( (columns[col][0]+columns[col][1]) < boardSize):
        for a in range(0, boardSize):
            b = col + 1 + a*boardSize
            if checkIfLegal(b, occupied)[0] == True:
                return b
    
    if diagonal == 0:
        if diagonals[0][0] == (boardSize-1) and ( (diagonals[0][0] + diagonals[0][1]) < boardSize):
            for a in range(0, boardSize):
                b = 1 + a*(boardSize+1)
                print(b)
                if checkIfLegal(b, occupied)[0] == True:
                    return b
    if diagonal == 1:
        if diagonals[1][0] == (boardSize-1) and ( (diagonals[1][0] + diagonals[1][1]) < boardSize):
            for a in range(0, boardSize):
                b = boardSize + a*(boardSize-1)
                if checkIfLegal(b, occupied)[0] == True:
                    return b

    # If everything else fails, pick a random cell like a human would or strategic positions
                                                                                                            # AI's last resort
    if centerTaken == False:                                                                                # We don't bother running the same calculation over and over if it's taken
        center = boardSize // 2 * (boardSize + 1) + 1
        if (boardSize % 2) == 1:
            if checkIfLegal(center, occupied)[0] == True:
                centerTaken = True
                return center
            elif checkIfLegal(center, occupied)[0] == False:
                centerTaken = True
        elif (boardSize % 2) == 0:
            centerTaken == 0                                                                                # Not actually taken, the center just doesn't exist
    corners = [1, boardSize, (boardSize-1)*boardSize + 1, boardSize**2]
    if cornersTaken == False:                                                                               # We don't bother running the same calculation over and over if it's taken
        for b in corners: 
            if checkIfLegal(b, occupied)[0] == True:
                return b
        if checkIfLegal(boardSize**2, occupied)[0] == False:
            cornersTaken == True
        
    if True:
        randomMove = computerMove(board, occupied)
        return randomMove

def main():
    global boardSize
    global rows
    global columns
    global diagonals

    print("Hello and welcome to the Tic-Tac-Toe Comp 208 challenge: Player against Computer.")

    
    while True:
        userInput = input("Start? (y/n) ")
        if userInput == "y" or userInput == "Y":
            break
        elif userInput == "n" or userInput == "N":
            exit()
        else:
            print("Invalid input, try again.")

    while True:                                                                                             # Only stops when we get a satisfying answer
        try:
            boardSize = int(input("Which size should the board be? (>= 3) "))
            if boardSize >= 3:
                break
        except ValueError:
            print("Please enter an integer.")
    
    board = dict([(a, f"{a:02.0f}") for a in range(1, boardSize**2+1)])                                     # For i in range, this creates a tuple with a key and value, adds it to a list which is then turned into a dictionary. The format string is used to create numbers "01", "02", and so on
    occupiedTiles = []
    previousMove = None
    print("The board is numbered from 1 to", boardSize**2, "as per the following:")
    displayBoard(board)
    print("Player starts first. Simply input the number of the cell you want to occupy. Player’s move is marked with X. Computer’s move is marked with O.")
    rows = [[0,0] for a in range(0, boardSize)]                                                             # For each row, we create sublists as described in line 2. Same with columns
    columns = [[0,0] for a in range(0, boardSize)]
    diagonals = [[0,0],[0,0]]  

    while True:
        # Here begins player's turn. AI's turn ends here.
        turn = 0                                                                                            # Set a flag for turns

        while True:                                                                                         # Only stops when we get a satisfying answer
            try:
                number = int(input("Which number of the board would you like to occupy? "))
                break
            except ValueError:
                print("Please enter an integer.")
        
        state, errorCode = checkIfLegal(number, occupiedTiles)
        
        if state == False:                                                                                  # Explains the errors to the player
            if errorCode == 1:
                print("Number is out of bounds, try again.")
            if errorCode == 2:
                print("Number is occupied already, try again.")
        
        elif state == True:                                                                                 # If move is legal...
            print("Number is legal, adding to the board...")
            board[number] = "x "                                                                            # Add it to the visual board
            occupiedTiles.append(number)                                                                    # We add it to the list of occupied cells
            displayBoard(board)                                                                             # Display the board

            appendCounters(number, turn)                                                                    # We add the value to rows, columns, and maybe diagonals
            row, col, diagonal = convertToArray(number)

            checkWinner((row, col, diagonal), occupiedTiles, turn)                                          # Again, 0 = player, 1 = computer. We check for a winner
            
            # Player turn ends here. Here begins the AI's turn
            turn = 1
            #moveAI = computerMove(board, occupiedTiles)

            moveAI = smartComputerMove(board, occupiedTiles, (row, col, diagonal), previousMove)            # AI plays against our move and with its previous move
            
            print("Computer has placed an o at cell", moveAI)

            board[moveAI] = "o "
            occupiedTiles.append(moveAI)
            displayBoard(board)

            appendCounters(moveAI, turn)
            previousMove = moveAI
            
            row, col, diagonal = convertToArray(moveAI)
            checkWinner((row, col, diagonal), occupiedTiles, turn)

            # AI turn ends here. Replace computerMove(board, occupiedTiles) with smartComputerMove to test either

main()