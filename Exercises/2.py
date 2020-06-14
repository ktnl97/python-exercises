num = int(input("Enter a number\n"))

print("%d is even %s" % (num, "even" if num % 2 == 0 else "odd")) if num%4 != 0 else  print("{0} is divisible by 4".format(num))

another_num = int(input("Enter another number\n"))

quotient, reminder = divmod(num, another_num)

print("{0} is {1} times {2}".format(num, quotient, another_num)) if(reminder == 0) else print("{0} when divided by {1} has a reminder of {2}".format(num, another_num, reminder))