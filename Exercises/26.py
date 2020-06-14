import tic_tac_toe_utils as utils
    
board = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

utils.display_board(board)
winner = utils.get_winner(board, [1,2], 0)
print("Player {0} is the winner".format(winner)) if  winner != 0 else print("We don't have a winner")