def get_unique(items):

    unique = lambda x: list(set(x))
    return unique(items)
print(get_unique([1, 2, 3, 4, 5, 5, 5, 5, 5,5]))

