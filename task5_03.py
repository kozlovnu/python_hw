# Создайте программу для игры в ""Крестики-нолики"".
import random

board = ['','x','0','x','0','x','0','x','0','x']

def Board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def InputPlayerLetter():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Choose letter x or o: ')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def WhoFirst():
    if random.randint(0,1) == 0:
        return 'Computer'
    else:
        return 'Human'

def Move(board, letter, move):
    board[move] = letter

def Winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le or
    bo[7] == le and bo[4] == le and bo[1] == le or
    bo[7] == le and bo[5] == le and bo[3] == le or
    bo[8] == le and bo[5] == le and bo[2] == le or
    bo[9] == le and bo[6] == le and bo[3] == le or
    bo[4] == le and bo[5] == le and bo[6] == le or
    bo[1] == le and bo[2] == le and bo[3] == le or
    bo[1] == le and bo[5] == le and bo[9] == le))

def BoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def FreeSpace(board, move):
    return board[move] == ' '

def PlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not FreeSpace(board, int(move)):
        print('Its your turn. Enter number from 1 to 9')
        move = input()
    return int(move)

def ChooseRandomMove(board, moveList):
    possibleMoves = []
    for i in moveList:
        if FreeSpace(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def ComputerMove(board, compLetter):
    if compLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1,10):
        boardCopy = BoardCopy(board)
        if FreeSpace(boardCopy,i):
            Move(boardCopy, compLetter, i)
            if Winner(boardCopy, compLetter):
                return i
    for i in range (1,10):
        boardCopy = BoardCopy(board)
        if FreeSpace(boardCopy,i):
            Move(boardCopy, playerLetter, i)
            if Winner(boardCopy, playerLetter):
                return i
    move = ChooseRandomMove(board, [1,3,7,9])
    if move != None:
        return move
    if FreeSpace(board, 5):
        return 5
    return ChooseRandomMove(board, [2,4,6,8])

def BoardFull(board):
    for i in range(1,10):
        if FreeSpace(board,i):
            return False
    return True

print('Game Tic-Tac-Toe')
while True:
    theBoard = [' ']*10
    playerLetter, compLetter = InputPlayerLetter()
    # compLetter = InputPlayerLetter()
    turn = WhoFirst()
    print(''+turn+' go\'s first')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'Human':
            Board(theBoard)
            move = PlayerMove(theBoard)
            Move(theBoard,playerLetter,move)
            if Winner(theBoard,playerLetter):
                Board(theBoard)
                print('You are the winner!')
                gameIsPlaying = False
            else:
                if BoardFull(theBoard):
                    Board(theBoard)
                    print('A draw')
                    break
                else:
                    turn = 'Computer'
        else:
            move = ComputerMove(theBoard, compLetter)
            Move(theBoard, compLetter, move)
            if Winner(theBoard, compLetter):
                Board(theBoard)
                print('Computer is the winner! You loose')
                gameIsPlaying = False
            else:
                if BoardFull(theBoard):
                    Board(theBoard)
                    print('A draw')
                else:
                    turn = 'Human'

    print('Try again? (y/n)')
    if not input().lower().startswith('y'):
        break