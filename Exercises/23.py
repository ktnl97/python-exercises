prime_numbers = set([int(number.strip()) for number in open("prime_numbers.txt", "r")])
happy_numbers = set([int(number.strip()) for number in open("happy_numbers.txt", "r")])
print(sorted(prime_numbers & happy_numbers))