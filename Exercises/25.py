numbers = [i for i in range(101)]
guess_count = 0
def get_guess_number(numbers):
    global guess_count
    guess_count += 1
    total_length = len(numbers)
    return numbers[total_length//2]

def get_first_half(numbers):
    return numbers[0: len(numbers)//2]

def get_second_half(numbers):
    return numbers[len(numbers)//2 + 1: len(numbers)]


result = 0

while True:
    guess_number = get_guess_number(numbers)
    print("Guess is {0}".format(guess_number))
    print("1. Too low\n2. Tow High \n3. Guessed it right!")
    result = int(input("Is the guess right?\n"))
    if(result == 1):
        numbers = get_second_half(numbers)
    elif(result == 2):
        numbers = get_first_half(numbers)
    elif(result == 3):
        print("It took {0} guesses to find the number".format(guess_count))
        break;
    else: 
        print("Invalid option")


    