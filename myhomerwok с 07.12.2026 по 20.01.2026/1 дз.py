a=input("Введите последновательность  чисел разделенных запятой")
number_b=[s.strip() for s in a.split(',')]
e=[int(num) for num in number_b]
my_list=e
my_tuple=tuple(e)
print("мой список", my_list)
print("мой чертеж", my_tuple)