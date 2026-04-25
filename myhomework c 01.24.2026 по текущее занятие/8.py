def sum_1(numbers):
    return sum(map(lambda x: x**2, numbers))
x = [1, 2, 3]
result = sum_1(x)
print(result)