from Util import get_random_word

def unhide_guessed_letter(guess_letters, word):
    display_text = ""
    for letter in word:
        if letter in guess_letters:
            display_text += letter + " "
        else:
            display_text += "_" + " "
    return display_text

hangman = []
allowed_incorrect_guesses = 0
incorrect_guesses = 0


def initialize_game():
    global hangman, allowed_incorrect_guesses, incorrect_guesses
    hangman = ["________ ", "|  |", "|   ", "|   ", "|   ", "|_______   "]
    allowed_incorrect_guesses = 6
    incorrect_guesses = 0


def display_hangman(incorrect_guess_no):
    if(incorrect_guess_no == 0):
        for i in hangman:
            print(i)
    if(incorrect_guess_no == 1):
        hangman[2] = "|  0"
        for i in hangman:
            print(i)
    if(incorrect_guess_no == 2):
        hangman[3] = "|  |"
        for i in hangman:
            print(i)
    if(incorrect_guess_no == 3):
        hangman[3] = "| /|"
        for i in hangman:
            print(i)
    if(incorrect_guess_no == 4):
        hangman[3] = "| /|\\"
        for i in hangman:
            print(i)
    if(incorrect_guess_no == 5):
        hangman[4] = "| /"
        for i in hangman:
            print(i)
    if(incorrect_guess_no == 6):
        hangman[4] = "| / \\"
        for i in hangman:
            print(i)

def play_hangman():
    global hangman, allowed_incorrect_guesses, incorrect_guesses
    initialize_game()
    word = (get_random_word()).lower()
    print(word)
    guess_letters = ""
    while incorrect_guesses != allowed_incorrect_guesses and not all([letter in guess_letters for letter in word]):
        print("*"*100)
        print(unhide_guessed_letter(guess_letters, word))
        print("Guess your letter: ")
        guess_letter = input()[0]
        print("*"*100)
        if guess_letter in guess_letters:
            incorrect_guesses += 1
            display_hangman(incorrect_guesses)
            continue
        if guess_letter in word:
            guess_letters += guess_letter
        else:
            incorrect_guesses += 1
            print("Incorrect!")
        display_hangman(incorrect_guesses)
    print("You guessed it correctly" if incorrect_guesses != allowed_incorrect_guesses else "You have exceeded the no. of allowed incorrect guesses. \nThe word was {0}".format(word))

while 1:
    play_hangman()
    print("Do you want to continue playing (y) or (n)?")
    if(input() != 'y'):
        break
    
