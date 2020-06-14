input_array = [1,2,49,3,15,4,1,2,15,6,10,12,13,14,12,10]
def distinct_by_list(input_array):
    result = []
    for i in input_array:
        if i not in result:
            result.append(i)
    return result

def distinct_by_set(input_array):
    return set(input_array)

print(distinct_by_list(input_array))
print(distinct_by_set(input_array))