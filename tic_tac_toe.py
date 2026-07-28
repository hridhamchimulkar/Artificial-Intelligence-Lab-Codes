INF = float('inf')
board = ['-'] * 9


def printBoard():
    for i in range(0, 9, 3):
        print(f"{board[i]} {board[i + 1]} {board[i + 2]}")
    print()


def Terminal():
    return '-' not in board


def Winner(player):
    lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for line in lines:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
        
    return False


def Minimax(isMax):
    if Winner('O'):
        return 1
    
    if Winner('X'):
        return -1
    
    if Terminal():
        return 0
    
    if isMax:
        value = -INF
        
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O'
                value = max(value, Minimax(not isMax))
                board[i] = '-'
        
        return value
    
    else:
        value = INF
        
        for i in range(9):
            if board[i] == '-':
                board[i] = 'X'
                value = min(value, Minimax(not isMax))
                board[i] = '-'
                
        return value
    
    
def BestMove():
    bestMove = -1
    bestValue = -INF
    
    for i in range(9):
        if board[i] == '-':
            board[i] = 'O'
            value = Minimax(False)
            board[i] = '-'
            
            if value > bestValue:
                bestMove = i
                bestValue = value
                
    return bestMove


print("Initial Board")
printBoard()

while True:
    pos = int(input("Your move: ")) - 1
    
    if board[pos] != '-':
        print("Move not allowed\n")
        continue
    
    board[pos] = 'X'
    printBoard()
    
    if Winner('X'):
        print("You won!")
        break
    
    if Terminal():
        print("Draw!")
        break
    
    print("Computer's move")
    move = BestMove()
    board[move] = 'O'
    printBoard()
    
    if Winner('O'):
            print("Computer won!")
            break
        
    if Terminal():
        print("Draw!")
        break