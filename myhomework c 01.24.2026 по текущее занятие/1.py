def filter_(numbers):

    return list(filter(lambda x: x % 2 == 0, numbers))
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_(numbers_list)
print(result)



