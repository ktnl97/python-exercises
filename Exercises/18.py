import Util
import random
import numpy
import string

random_number = [1,0,3,8]
guesses = 0
print(random_number)
def match_numbers(number):
    global random_number
    cows = 0
    bulls = 0
    for i in range(len(random_number)):
        if number[i] == random_number[i]:
            cows += 1
        elif number[i] in random_number:
            bulls += 1
    print("{0} cows, {1} bulls".format(cows, bulls))

def convert_to_array(number):
    return [ int(i) for i in number]


print("Welcome to the Cows and Bulls Game!")

while 1:
    number = convert_to_array(input("Enter a number\n"))
    guesses += 1
    if random_number == number:
        break
    match_numbers(number)
print("Guessed it! \nYou took {0} guesses".format(guesses))



