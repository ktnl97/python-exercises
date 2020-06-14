import json
birthday_dictionaries = __import__('33')

birthday_dict = dict()
with open("birthdays.json") as input_file:
    birthday_dict = json.load(input_file)

def upsert_birthday_info(birthday_dict):
    print("Enter the name of the person:")
    name = input()
    print("Enter the birth day of the person:")
    birthday = input()
    birthday_dict[name] = birthday

    with open("birthdays.json", "w") as output_file:
        json.dump(birthday_dict, output_file)

def main():
    upsert_birthday_info(birthday_dict)
    birthday_dictionaries.find_birthday(birthday_dict)

main()
