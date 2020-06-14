default_value = 'O'
default_players = ['X', 'Y']

def create_board(no_of_rows, no_of_columns, default_value = default_value):
    return [[default_value for _ in range(3)] for __ in range(3)]

def get_winner(board, valid_players = default_players, default_value = default_value):
    winner = default_value
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] in valid_players:
            winner = board[i][0]
            break
        elif board[0][i] == board[1][i] == board[2][i] in valid_players:
            winner = board[0][i]
            break
        elif board[0][0] == board[1][1] == board[2][2] in valid_players:
            winner = board[0][0]
            break
        elif board[0][2] == board[1][1] == board[2][0] in valid_players:
            winner = board[0][2]
            break
    return winner

def print_horizontal_lines(dimension):
    horizontal = " "
    for _ in range(dimension):
        horizontal += "-"*dimension+" "
    print(horizontal)

def print_vertical_lines(dimension, board):
    vertical = ""
    spaces_count = dimension // 2
    for i in range(dimension):
        vertical += "|"+ " "*spaces_count + str(board[i]) + " "*spaces_count
    vertical += "|"
    print(vertical)

def display_board(board):
    length = len(board)
    for i in range(length):
        print_horizontal_lines(length)
        print_vertical_lines(length, board[i])
    print_horizontal_lines(length)

def capture_next_move(board, current_player_coin, default_value = default_value):
    while 1:
        print("*"*100)
        print("Player {0}: Enter the co-ordinates in row, column format \n(Co-ordinates can be from 1 to 3)".format(current_player_coin))
        user_input = input().split(",")
        row, column = int(user_input[0]), int(user_input[1])
    
        if(board[row-1][column-1] != default_value):
            print("This cell is already taken.")
            continue
        board[row-1][column-1] = current_player_coin
        break;
