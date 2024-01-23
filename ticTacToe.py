from functions import display_board as display
from functions import toggle_player as toggle
from functions import check_for_win
from functions import check_for_tie
from functions import toggle_player

print('Welcome players!!! Classic Tic Tac Toe Game')


playing = True #This variable is for if players want to play again
while playing:
    initialToken = False
    while initialToken != 'X' and initialToken != 'O':
        initialToken = input("Player 1 --- Do you want 'X' or 'O' \n").capitalize()

    gameOn = True #This variable is for tracking game status
    player = 'Player 1' #initialize player
    token = initialToken #initialize token
    tie = False #This variable is for determining and tracking a tie game
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #Initialize board

    while gameOn:
        display(board)

        position = True
        while position:
            players_choice = str(input('{}: Choose a positon to place your token \n'.format(player)))
            if players_choice in board:
                board[int(players_choice) - 1] = token
                position = False
                
        if check_for_win(token, board):
            gameOn = False
            display(board)
        elif check_for_tie(board):
            gameOn = False
            tie = True
        else:
            (player, token) = toggle_player(player, token)
            print('\n'*50)

    if tie:
        print('Game Over. Game has ended in a tie!!!')
    else:
        print('Game over. {} wins!!!!'.format(player))
    
    playAgain = input('Do you want to play again? "Y" or "N" \n').capitalize()
    if playAgain == 'N':
        playing = False
        
