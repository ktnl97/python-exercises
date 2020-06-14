num = int(input("Enter a number\n"))
print(list(filter(lambda x: num%x == 0, list(range(1,num//2 + 1)))))