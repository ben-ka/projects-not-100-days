"""
Tic Tac Toe Player
"""

import math

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
    countX = 0
    countO = 0
    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1
    if countX <= countO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = []
    for row in board:
        for cell in row:
            if cell == EMPTY:
                indexes = (board.index(row), row.index(cell))
                actionSet.append(indexes)


    return actionSet
    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    players_turn = player(board)
    try:
        copy = board
        (copy[action[0]])[action[1]] = players_turn
        
        return copy
    
    except IndexError:
        raise IndexError

    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


    
    def CheckRowWin(board):
        countX = 0
        countO = 0
        for row in board:
            for cell in row:
                if cell == X:
                    countX += 1
                elif cell == O:
                    countO += 1
            if countX == 3:
                return X
            elif countO == 3:
                return O
            countO = 0
            countX = 0
        return None
    
    def CheckColumnWin(board):
        countX = 0
        countO = 0

        
        for index in range(0,3):
            for row in board:
                if row[index] == X:
                    countX += 1
                elif row[index] == O:
                    countO += 1
            if countX == 3:
                return X
            elif countO == 3:
                return O
            
            countX = 0
            countO = 0
        return None
    
    def CheckDiagonalWin(board):
        countX = 0
        countO = 0

        for index in range(0,3):
            for row in board[index:index + 1]:
                if row[index] == X:
                    countX += 1
                elif row[index] == O:
                    countO += 1
        if countX == 3:
            return X
        elif countO == 3:
            return O
        countX = 0
        countO = 0
        
        for index in range(2,-1,-1):
            for row in board[index:index + 1]:
                if row[2-index] == X:
                    countX += 1
                elif row[2-index] == O:
                    countO += 1
        if countX == 3:
            return X
        elif countO == 3:
            return O
        
        countX = 0
        countO = 0
        return None
    

    rowWin = CheckRowWin(board)
    if rowWin != None:
        return rowWin
    columnWin = CheckColumnWin(board)
    if columnWin != None:
        return columnWin
    diagonalWin = CheckDiagonalWin(board)
    if diagonalWin != None:
        return diagonalWin
    
    return None


    


            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    gameWinner = winner(board)
    if gameWinner != None:
        return True
    
    possibleActions = actions(board)
    if len(possibleActions) == 0:
        return True
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == False:
        return 0
    gameWinner = winner(board)
    if gameWinner == None:
        return 0
    if gameWinner == X:
        return 1
    if gameWinner == O:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def MaxValue(board):
        v = -999
        
        action_values = {}
        for action in actions(board):
            action_values[action] = MinValue(utility(result(board,action)))
            v = max(v,action_values[action])
            
        
        for action in action_values.keys():
            if action_values[action] == v:
                return action
        
    
    def MinValue(board):
        v = 999
        action_values = {}
        for action in actions(board):
            action_values[action] =  MaxValue(utility(result(board, action)))
            v = min(v,action_values[action] )
            
            
        for action in action_values.keys():
            if action_values[action] == v:
                return action

    if terminal(board):
        return None
    if player(board) == X:
        return MaxValue(board)
    if player(board) == O:
        return MinValue(board)
    
    

