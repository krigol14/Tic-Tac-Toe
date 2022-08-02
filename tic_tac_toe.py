# TIC TAC TOE GAME IN PYTHON

# populating the board list
board = [' ' for i in range(10)]

def compMove():
    # is there a move that the computer can do to win, if yes do that move to win the game
    # is there a move that the player can do to win, if yes move to that position so as the player does not win
    # pick a corner to move, if there aren't any free corners to move then move to center, if center is taken too then move to any free space on the edges

    # x is the index and letter is the actual value in the enumerate(board)
    # enumerate(list) gives us the indexes and the actual value in the list we pass into it
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # find if there is a position the computer can move so that it wins
    for let in ['O', 'X']:
        for i in possibleMoves:
            # we just want to make a copy of board and not change it
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    # move to the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # move to the center of the board
    if 5 in possibleMoves:
        move = 5
        return move

    # move to the edges
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def insertLetter(letter, position):
    board[position] = letter

# function that checks if a position of the board is free or not
def spaceIsFree(position):
    # this is going to return a boolean value true or false
    return board[position] == ' '

# function that prints the board to play the game
def printBoard(board):
    print('    |    |')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('    |    |')

# function to check if someone has won
def isWinner(board, letter):
    # if one of the below conditions is true the isWinner function returns true
    return(
    (board[1] == letter and board[2] == letter and board[3] == letter) or # vertical 1
    (board[4] == letter and board[5] == letter and board[6] == letter) or # vertical 2
    (board[7] == letter and board[8] == letter and board[9] == letter) or # vertical 3
    (board[1] == letter and board[4] == letter and board[7] == letter) or # horizontal 1
    (board[2] == letter and board[5] == letter and board[8] == letter) or # horizontal 2
    (board[3] == letter and board[6] == letter and board[9] == letter) or # horizontal 3
    (board[1] == letter and board[5] == letter and board[9] == letter) or # diagonal left
    (board[3] == letter and board[5] == letter and board[7] == letter))   # diagonal right

# returns true or false if the board is full or not
def isBoardFull(board):
    # if we have more than one blank spaces then our board is not foul (we started with one blank space)
    if board.count(' ') > 1:
        return False
    else:
        return True

def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an X into (1 - 9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is occupied!")
            else:
                print("Please type a number within the range 1-9!")
        except:
            print("Please type a number!")

def main():
        print("Welcome to Tic Tac Toe!")
        printBoard(board)

        while not (isBoardFull(board)):
            # check if the computer won
            if not (isWinner(board, 'O')):
                playerMove()
                # printBoard(board)
            else:
                print("Sorry O's won this time!")
                break

            # check if the player won
            if not (isWinner(board, 'X')):
                move = compMove()
                if move == 0:
                    print("Tie game!")
                else:
                    insertLetter('O', move)
                    print("Computer placed an O in position ", move)
                    printBoard(board)
            else:
                print("Good job!")
                break

        if isBoardFull(board):
            print("Tie game!")

main()

while True:
    ans = input("\nDo want to play again? (type 'yes' or 'no'): ")
    if ans == "yes":
        board = [' ' for i in range(10)]
        main()
    else:
        break
    