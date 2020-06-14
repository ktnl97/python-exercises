def get_input():
        return int(input("Enter a number: "))

def get_fibonacii_series(count):
    series = [1,1]
    if count <= 2:
        return series[0:count]
    for i in range(2, count):
        series.append(series[i-1] + series[i-2])
    return series

print(get_fibonacii_series(get_input()))

