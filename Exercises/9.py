import random
random_num = random.randint(0,9)
guesses = 1
guess_num = 0
while guess_num != "exit":
        guess_num = input("Guess the number\n")
        if not guess_num.isdigit():
            print("Invalid input")
            continue
        guess_num = int(guess_num)
        if random_num > guess_num:
            print("Too low")
        elif random_num < guess_num:
            print("Too High")
        else:
            print("You guessed it right! after {0} guesses".format(guesses))
            break
        guesses+=1
        