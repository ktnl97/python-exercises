
import json
birthday_dict = {
    'Anu': '01/07/1997',
    'Banu': '06/02/1996',
    'Chitra': '03/05/1992',
    'Divya': '25/04/1999'
}

def find_birthday(birthday_dict):
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for name in birthday_dict.keys():
        print(name)
    print("Who's birthday do you want to look up?")
    name = input()
    print("{0}'s birthday is {1}".format(name, birthday_dict[name]) if name in birthday_dict else "{0}'s birthday is not found".format(name))

def main():
    find_birthday(birthday_dict)

if __name__ == "__main__":
    main()
