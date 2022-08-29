from board import board, printBoard

playerSymbol = 'O'
botSymbol = 'X'

print("=== Tic Tac Toe ===")
print("Welcome to Tic Tac Toe, instructions are as follows:")
print("1) Bot goes first following your counter by entering a number in one of these positions:")
print("   1|2|3")
print("   -+-+-")
print("   4|5|6")
print("   -+-+-")
print("   7|8|9")
print("2) Once you have 3 entries next to each other in whatever direction before your opponent, you win!")
print()
print("Let's begin!")
print()

# Helper method to check board if the given position is free
def checkFreeSpace(position):
    if (board[position] == ' '):
        return True
    else:
        return False

# Helper method to check if the game is a draw
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    
    return True

# Helper method to check if there is a win somewhere
def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

# Helper method to determine when to stop recursion
def checkWhoWon(symbol):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == symbol):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == symbol):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == symbol):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == symbol):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == symbol):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == symbol):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == symbol):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == symbol):
        return True
    else:
        return False

# Insert the given position by player symbol and check game state
def insertMove(symbol, position):
    if checkFreeSpace(position):
        board[position] = symbol
        printBoard(board)

        if checkWin():
            if (symbol == 'X'):
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        if checkDraw():
            print("Draw!")
            exit()

        return
    else:
        print("Can't insert there! Try again.")
        position = int(input("Enter new position: "))

        insertMove(symbol, position)
        return

# Asks for the player's next move
def playerMove():
    while True:
        try:
            position = int(input("Enter the position for 'O': "))
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            insertMove(playerSymbol, position)
            break

    return

# Determines next move of bot
def botMove():
    bestScore = -1000 # Start with low score for maximizing (wheter it is -1000 or -15000 doesn't really matter)
    bestMove = 0 # Init var

    # Play every empty move to minimax for the best move
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = botSymbol

            score = minimax(board, False) # Start minimizing for it is set to false
            board[key] = ' ' # Restore move to empty for it has been minimaxed

            # Set the minimaxed move
            if (score > bestScore):
                bestScore = score
                bestMove = key

    print("Bot moved on: ", bestMove)
    insertMove(botSymbol, bestMove) # Use the minimaxed move

    return

# This algorithm will check every possible positions, assign scores to each and pick the position with the best score
def minimax(board, isMaximizing):
    # Positive value for if bot wins, negative value for if bot loses so it knows not to make such moves
    if checkWhoWon(botSymbol):
        return 100
    elif checkWhoWon(playerSymbol):
        return -100
    elif checkDraw():
        return 0

    # Check who is playing
    if isMaximizing:
        bestScore = -1000 # Start with low score for maximizing (wheter it is -1000 or -15000 doesn't really matter)

        for key in board.keys():
            if (board[key] == ' '):
                board[key] = botSymbol
                
                score = minimax(board, False) # Start minimizing for it is set to false
                board[key] = ' ' # Restore move to empty for it has been minimaxed

                if (score > bestScore):
                    bestScore = score

        return bestScore
    else:
        bestScore = 1000 # Start with high score for minimizing

        for key in board.keys():
            if (board[key] == ' '):
                board[key] = playerSymbol
                
                score = minimax(board, True) # Start maximizing for it is set to true
                board[key] = ' ' # Restore move to empty for it has been minimaxed

                if (score < bestScore):
                    bestScore = score

        return bestScore

# Keep playing until either the player or the bot have won
while not checkWin():
    botMove()
    playerMove()
