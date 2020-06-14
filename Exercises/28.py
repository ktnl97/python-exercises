def max(numbers):
    highest = numbers[0]
    for number in numbers[1:]:
        if number >= highest:
            highest = number
    return highest
      

print(max([12,34,34]))