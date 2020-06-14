import random
import string
import Util as Util

totalLength = Util.get_int_input("Enter the length of your password:")

possible_characters = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]

def generate_random_characters(length):
    random_characters = [ random.choice(possible_characters[ i % 4]) for i in range(length)]
    random.shuffle(random_characters)
    return random_characters

def get_strong_password(length):
    return "".join(generate_random_characters(length))

print(get_strong_password(totalLength))

