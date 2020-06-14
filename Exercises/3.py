num = int(input("Ente a number\n"));
print(list(filter(lambda x: x < num, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])))