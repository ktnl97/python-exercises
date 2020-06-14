import json
import random
import string
from datetime import datetime
from collections import Counter

def seed_birthdays():
    birthday_dict = dict()
    for _ in range(100):
        name = "".join(random.sample(list(string.ascii_lowercase) + list(string.ascii_uppercase), random.randint(6,12)))
        birthday = "{}/{}/{}".format(random.randint(1,28),random.randint(1,12),random.randint(1990,2000))
        birthday_dict[name] = birthday

    with open("birthdays.json", "w") as output_file:
        json.dump(birthday_dict, output_file)


def get_month_count():
    birthday_dict = dict()
    with open("birthdays.json") as input_file:
        birthday_dict = json.load(input_file)
    months = [(datetime.strptime(date, '%d/%m/%Y')).strftime('%B') for date in birthday_dict.values()]
    return Counter(months)

def main():
    seed_birthdays()
    print(get_month_count())

if __name__ == "__main__":
    main()