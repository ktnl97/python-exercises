inputString = input("Enter a string\n")
print("{0}".format("Yes" if inputString == inputString[::-1] else "No"))