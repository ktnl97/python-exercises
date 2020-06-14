dimension = int(input(("Enter the Tic Tac Toe grid dimension\n")))

def print_horizontal_lines():
    horizontal = " "
    for _ in range(dimension):
        horizontal += "-"*dimension+" "
    print(horizontal)

def print_vertical_lines():
    vertical = ""
    for _ in range(dimension+1):
        vertical += "|"+ " "*dimension
    print(vertical)

def draw_board(dimension):
    for _ in range(dimension):
        print_horizontal_lines()
        print_vertical_lines()
    print_horizontal_lines()

draw_board(dimension)