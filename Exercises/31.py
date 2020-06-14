from Util import get_random_word

def unhide_guessed_letter(guess_letters, word):
    display_text = ""
    for letter in word:
        if letter in guess_letters:
            display_text += letter + " "
        else:
            display_text += "_" + " "
    return display_text

def play_hangman():
    word = (get_random_word()).lower()
    print(word)
    guess_letters = ""
    while not all([letter in guess_letters for letter in word]):
        print("*"*100)
        print(unhide_guessed_letter(guess_letters, word))
        print("Guess your letter: ")
        guess_letter = input()[0]
        print("*"*100)
        if guess_letter in guess_letters:
            print("Letter already guessed")
            continue
        if guess_letter in word:
            guess_letters += guess_letter
        else:
            print("Incorrect!")
    print("You guessed it correctly")

play_hangman()