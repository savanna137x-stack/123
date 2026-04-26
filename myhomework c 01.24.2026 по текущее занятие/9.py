
def main(dict_list, key):
    return list(map(lambda d: d.get(key), dict_list))

my_list= [{"name": "anton", "age": 77}]
my_key = "name"
result = main(my_list, my_key)
print(result)



