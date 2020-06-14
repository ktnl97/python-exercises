def get_sanitized_list(input_list):
    return [input_list[0], input_list[-1]]
a = [5, 10, 15, 20, 25]
print(get_sanitized_list(a))
