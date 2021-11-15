import random

board = [' ' for x in range(10)]

#   Insters letter into pos
def insterLetter(letter, pos):
    global board
    board[pos] = letter

#   Checks if space is free
def spaceIsFree(pos):
    return board[pos] == ' '

#   Board print
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#   Checks if a player has won
def isWinner(bo, le):
    #   << VERY UNCLEAN LINE OF CODE >>
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le))

#   Checks player input, and if move is valid add move to board
def playerMove():
    run = True
    while run:
        move = input('<< Please type your wanted coordinates to place an X! (1-9) >>')
        
        #   Tries user input
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insterLetter("X", move)
                else:
                    print("<< ERROR: PASE IS ALREADY TAKEN >>")
                    
            else:
                print("<< ERROR: INVALID COORDINATES WHERE GIVEN >>")
            
        except:
            print("<< ERROR: INVALID COORDINATES! >>")
            

def compMove():
    #   Checks for possible moves
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0    #   Auto tie if this is not changed
    
    #   Checks if O or X is about to win
    for let in ["O", "X"]:
        for i in possibleMoves:             #   Checks for WhiteSpaces
            boardCopy = board[:]            #   Copies Board
            boardCopy[i] = let
            if isWinner(boardCopy, let):    #   Check if anyone can make a winning move  
                move = i
                return move
            
    #--------------------------------
    #   If the center is open, move there
    if 5 in possibleMoves:
        move = 5
        return move
    
    #---------------------------------
    #   Checks if any corners are open
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    #   If coners open move to a corner        
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    #--------------------------------
    #   Checks if any edges are open
    edgessOpen = []
    for i in edgessOpen:
        if i in [2, 4, 6, 8]:
            edgessOpen.append(i)
    #   If coners open move to a corner        
    if len(edgessOpen) > 0:
        move = selectRandom(edgessOpen)
        return move
    
#   Returs a random item from given list
def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
    
#   Checks if board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    printBoard(board)
    
    #   If its not a tie
    while not(isBoardFull(board)):
        #   If O didn't win let X play
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        
        #   Checks if O has won
        else:
            print("<< O is the winner! >>")
            break;
    
        #   If X didn't win let O play
        if not (isWinner(board, 'O')):
            move = compMove()
            if move == 0:
                print("<< Game is a tie! >>")
                
            else:
                insterLetter('O', move)
                print(f"<< CPU placed an O in position: {move} >>")
                printBoard(board)
        
        #   Checks if X has won
        else:
            print("<< X is the winner! >>")
            break;
    
    #   If it is a tie
    if isBoardFull(board):
        print('<< Game is a tie! >>')
      
      
#   Calls main to start the game   
main()