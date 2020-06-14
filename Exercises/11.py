def get_input():
        return int(input("Enter a number: "))

def get_divisors(number):
    return list(filter(lambda x: number%x == 0, list(range(1,number//2 + 1))))

num = get_input()
divisors= get_divisors(num)
print("{0} is {1} prime number".format(num, "a" if len(divisors) == 1 else "not a"))