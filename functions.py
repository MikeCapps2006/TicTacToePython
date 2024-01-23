# winning_combinations = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9]]
def check_for_win(token, board):
    return ((board[6] == token and board[7] == token and board[8] == token) or 
            (board[5] == token and board[4] == token and board[3] == token) or
            (board[6] == token and board[4] == token and board[2] == token) or
            (board[8] == token and board[5] == token and board[2] == token) or
            (board[7] == token and board[4] == token and board[1] == token) or
            (board[8] == token and board[4] == token and board[0] == token) or
            (board[6] == token and board[3] == token and board[0] == token) or
            (board[2] == token and board[1] == token and board[0] == token))

def check_for_tie(board):
    tie = False
    for pos in board:
        if pos != 'X' and pos != 'O':
            return tie
    tie = True
    return tie

def toggle_token(token):
    if token == 'X':
        token = 'O'
    else:
        token = 'X'
    return token

def toggle_player(player, token):
    if player == 'Player 1':
        player = 'Player 2'
    else: player = 'Player 1'
    token = toggle_token(token)
    return (player, token)
    

def display_board(board):
    dict = {'1': board[0],
            '2': board[1],
            '3': board[2],
            '4': board[3],
            '5': board[4],
            '6': board[5],
            '7': board[6],
            '8': board[7],
            '9': board[8]
            }
    print('\n')
    print(dict['7'] + ' | ' + dict['8'] + ' | '+ dict['9'])
    print('─' * 10)
    print(dict['4'] + ' | ' + dict['5'] + ' | '+ dict['6'])
    print('─' * 10)
    print(dict['1'] + ' | ' + dict['2'] + ' | '+ dict['3'])
    print('\n')