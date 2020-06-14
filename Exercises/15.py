delimiter = " "
def get_string():
    return input("Enter a long string: ")

def get_reversed_string(input_string):
    return delimiter.join(input_string.split(delimiter)[::-1])

print(get_reversed_string(get_string()))