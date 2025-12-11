import random

def print_board(board):
    i=0
    for row in board:
        print(' | '.join(row))
        if i<2:
            print('-'*9)
        i+=1


print("Write as 'x y' where x is row number and y is column number")
def player_move(board):
    while True:
        x,y=map(int,input("Enter row and column numbers to place X (0-2 for both): ").split())
        if 0<=x<=2 and 0<=y<=2 and board[x][y]==' ':
            board[x][y]='X'
            break
        else:
            print("Invalid move. Try again.")
            
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None


def available_moves(board):
    moves=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                moves.append((i,j))
    return moves

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, is_maximizing, depth, max_depth=None):
    """Recursive minimax with optional depth limit for difficulty."""
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_full(board):
        return 0

    # Stop recursion early based on difficulty (depth limit)
    if max_depth is not None and depth >= max_depth:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for x, y in available_moves(board):
            board[x][y] = 'O'
            score = minimax(board, False, depth + 1, max_depth)
            board[x][y] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for x, y in available_moves(board):
            board[x][y] = 'X'
            score = minimax(board, True, depth + 1, max_depth)
            board[x][y] = ' '
            best_score = min(score, best_score)
        return best_score
    
def ai_move(board, difficulty='hard'):
    moves = []
    if difficulty == 'easy':
        max_depth = 1
    elif difficulty == 'medium':
        max_depth = 3
    else:
        max_depth = None
    for move in available_moves(board):
        x, y = move
        board[x][y] = 'O'
        score = minimax(board, False, 0, max_depth)
        board[x][y] = ' '
        moves.append((score, move))

    # Sort by score
    moves.sort(key=lambda x: x[0])
    
    # Difficulty control
    if difficulty == 'easy':
        # Choose a completely random move
        chosen_move = random.choice(moves)[1]
    elif difficulty == 'medium':
        # Choose from top 2 moves (semi-smart)
        chosen_move = random.choice(moves[-2:])[1] if len(moves) >= 2 else moves[-1][1]
    else:
        # Hard mode → choose the best move (perfect play)
        chosen_move = moves[-1][1]

    # Place AI move
    board[chosen_move[0]][chosen_move[1]] = 'O'
    return board