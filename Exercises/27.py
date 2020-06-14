import tic_tac_toe_utils as utils

no_of_rows = 3
no_of_columns = no_of_rows

board = utils.create_board(no_of_rows, no_of_columns)
utils.display_board(board)
players = ['X', 'Y']

current_player = 0
while any([utils.default_value in x for x in board]):
    utils.capture_next_move(board,players[current_player])
    current_player = 1 - current_player
    utils.display_board(board)