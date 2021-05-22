"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0

    for rows in board:
        for colums in rows:
            if colums == X:
                X_count +=1
            elif colums == O:
                O_count += 1
    
    if X_count <= O_count:
        return X
    else:
        return O


    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    validMove = set()

    for i in range (3):
        for j in range (3):
            if board[i][j] == EMPTY:
                validMove.add((i, j))

    return validMove

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    boardCopy = copy.deepcopy(board)

    if boardCopy[action[0]][action[1]] != EMPTY:
        raise Exception("Place of action must be EMPTY")
    else:
        boardCopy[action[0]][action[1]] = player(board)
    
    return boardCopy
        
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY):
            return  board[i][0]
        if (board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY):
            return board[0][i]
        

    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) and board[1][1] != EMPTY):
        return board[1][1]
    

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True
     
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        score = -math.inf
        bestAction = None

        for action in actions(board):

            minVal = minValue(result(board, action))

            if minVal > score:
                score = minVal
                bestAction = action

        return bestAction

           

    elif player(board) == O:
        score = math.inf
        bestAction = None

        for action in actions(board):

            maxVal = maxValue(result(board, action))

            if maxVal < score:
                score = maxVal
                bestAction = action

        return bestAction

    raise NotImplementedError

def maxValue (board):

    if terminal(board):
        return (utility(board))

    num = -math.inf

    for action in actions(board):
        num = max (num, minValue(result(board,action)))

    return num


def minValue (board):

    if terminal(board):
        return (utility(board))

    num = math.inf

    for action in actions(board):
        num = min (num, maxValue(result(board,action)))

    return num