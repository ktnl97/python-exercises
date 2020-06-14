import tic_tac_toe_utils as utils

no_of_rows = 3
no_of_columns = no_of_rows
players = utils.default_players
score_board = dict.fromkeys(players, 0)
current_player_count = 1

def initialize_game():
    global current_player_count
    current_player_count = 1

def get_current_player():
    global current_player_count
    current_player_count = 1 - current_player_count
    return players[current_player_count]

while 1:
    board = utils.create_board(no_of_rows, no_of_columns)
    utils.display_board(board)
    while 1:
        current_player = get_current_player()
        utils.capture_next_move(board,current_player)
        winner = utils.get_winner(board)
        utils.display_board(board)
        if(winner in players):
            score_board[current_player] = score_board[current_player] + 1
            print("Player {0} has won the game!!!".format(current_player))
            break
        if(not any([utils.default_value in x for x in board])):
            print("This game is a draw!")
            break
    print("Do you want to continue playing (y) or (n)?")
    if input() != 'y':
        print("Final results :")
        print(score_board)
        break
    initialize_game()
