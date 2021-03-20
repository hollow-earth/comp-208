# This code could be made a LOT more efficient with numpy arrays instead of creating multiple lists, one for each row.

# We use a dictionary with dict [row #] = (# x, # o), dict [column #](#x, #o), dict[diagonal 1/2] (#x, #o)

def displayBoard(board):
    # Row length = 5, switch every 5
    i = 1
    while i < 26:
        print(board[i], board[i+1], board[i+2], board[i+3], board[i+4], sep="  ")
        i += 5

#def checkIfLegal(number, board):
    #aaaaaa

#def checkWinner(board):
    #bruh

#def computerMove(board):
    #a

#def smartComputerMove(board):
    #s

def main():
    board = {1:"01", 2:"02", 3:"03", 4:"04", 5:"05", 6:"06", 7:"07", 8:"08", 9:"09", 10:"10", 11:"11", 12:"12", 13:"13", 14:"14", 15:"15", 16:"16", 17:"17", 18:"18", 19:"19", 20:"20", 21:"21", 22:"22", 23:"23", 24:"24", 25:"25"}
    occupiedTiles = []
    print("Hello and welcome to the Tic-Tac-Toe Comp 208 challenge: Player against Computer.\nThe board is numbered from 1 to 25 as per the following:")
    displayBoard(board)
    print("Player starts first. Simply input the number of the cell you want to occupy. Player’s move is marked with X. Computer’s move is marked with O.")
    while True:
        userInput = input("Start? (y/n) ")
        if userInput == "y" or userInput == "Y":
            #valve please fix
            break
        elif userInput == "n" or userInput == "N":
            exit()
        else:
            print("Invalid input, try again.")

main()