def binary_search(array_of_numbers, min, max, number): 
    if max >= min: 
        mid = (max + min) // 2
        if array_of_numbers[mid] == number: 
            return True 
        elif array_of_numbers[mid] > number: 
            return binary_search(array_of_numbers, min, mid - 1, number) 
        else: 
            return binary_search(array_of_numbers, mid + 1, max, number) 
    else: 
        return False
  
array_of_numbers = [ 2, 3, 4, 10, 40 ] 
number = 2
  
print("Element is {0} in the given array".format("present" if binary_search(array_of_numbers , 0, len(array_of_numbers)-1, number)  else "not present"))