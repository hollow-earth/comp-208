from random import *
def displayBoard(board):    
    string = ""
    pos=0
    length=5
    for i in range(length):
        string=''
        for x in range(length):
            string+=str(board[pos+1])
            if (pos+1) < 10:
                string+=' '
            if x < length-1:
                string+='|'
            pos+=1
        print(string)
        if i<length-1:
            print('--' + (length-1)*'+--')
    return board

def checkIfLegal(number, board):
    if number > 25:
        print("The number you have picked is out of range")
        return False
    elif board[number]=="X" or board[number]=="O" or board[number]==number:
        return True 
    else:
        print("It is the number of an already occupied cell")
        return False

def checkWinner(board):
    row=0
    col=0
    count=0
    for i in range(5):
        if board[1+row]==board[2+row]==board[3+row]==board[4+row]==board[5+row]:
            if board[1+row]=='X ':
                print("Congratulations. Player wins.")
            else:
                print("Congratulations. Computer wins.")
            return True
        row+=5
        if board[col+1]==board[col+6]==board[i+11]==board[i+16]==board[i+21]:
            if board[col+1]=='X ':
                print("Congratulations. Player wins.")
            else:
                print("Congratulations. Computer wins.")
            return True
        col+=1
    for i in range(1,25):
        if board[i]=='X ' or board[i]=='O ':
            count+=1
    print(count)       
    if count==25:
        print("The game has ended in a tie")
        quit()
    if board[1]==board[7]==board[13]==board[19]==board[25]:
        if board[1]=='X':
            print("Congratulations. Player wins.")
        else:
            print("Congratulations. Computer wins.")
        return True
    elif board[5]==board[9]==board[13]==board[17]==board[21]:
        if board[5]=='X ':
            print("Congratulations. Player wins.")
        else:
            print("Congratulations. Computer wins.")
        return True
    else:
        return False

def computerMove(board):
    cmpMove=randint(1,25)
    while board[cmpMove] !=cmpMove:
        cmpMove=randint(1,25)
    return cmpMove
    

#def smartComputerMove(board):
    



    
        
def main():
    board = {}
    length=5
    for i in range(length*length):
        board[i+1] = i+1 
    print("Hello and welcome to the Tic-Tac-Toe Comp 208 challenge: Player against Computer.")
    print("The board is numbered from 1 to 25 as per the following:")
    displayBoard(board)
    print("Player starts first. Simply input the number of the cell you want to occupy."
    ,"Player’s move is marked with X. Computer’s move is marked with O.")
    
    userInput=input("Start? (y/n):")
    if userInput=="n":
        quit()
    while checkWinner(board)==False:
        number=int(input("Which cell would you like to occupy: "))
        while checkIfLegal(number, board)==False:
            number=int(input("Please enter a new cell again:"))
            checkIfLegal(number,board)
        print("Player's move")
        board[number]='X '    
        displayBoard(board)
        print("Computer's move")
        board[computerMove(board)]='O '
        displayBoard(board)
        
        

        
main()


