def find_common_elements(list1, list2):
    common = set(list1) & set(list2)
    return list(common)

print(find_common_elements([1, 2,6,7], [3, 4, 5, 6]))
