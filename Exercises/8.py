def is_current_player_winner(player, opposite_player):
    return opposite_player == game_rules[player]

def declare_result(result):
    global quit
    print(result)
    quit = input("Do you want to quit? Yes or No\n")

quit = "No"
game_rules = {
    'rock' : 'scissors',
    'scissors' : 'paper',
    'paper' : 'rock'
}
while quit not in ["Yes", "yes"]:
    player1Choice = input("Player 1: Enter your choice\n")
    if (player1Choice not in game_rules.keys()):
        print("{0}: Invalid option".format(player1Choice))
        continue
    player2Choice = input("Player 2: Enter your choice\n")
    if (player2Choice not in game_rules.keys()):
        print("{0}: Invalid option".format(player2Choice))
    elif player1Choice == player2Choice:
        declare_result("Match Drawed")
    elif player1Choice == game_rules[player2Choice]: 
        declare_result("Player 2 wins")
    else:
       declare_result("Player 1 wins")





