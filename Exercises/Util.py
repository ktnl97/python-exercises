import random
def get_int_input(message):
        return int(input(message))

def get_random_word():
    return (random.choice(words))
words = [word.strip() for word in open("dictionary.txt").readlines()]