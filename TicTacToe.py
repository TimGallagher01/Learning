board = ["-", "-", "-"
         "-", "-", "-"
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


# printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    printBoard(board)

# take payer input

# check for win or tie

# switch the player

# check for win or tie again