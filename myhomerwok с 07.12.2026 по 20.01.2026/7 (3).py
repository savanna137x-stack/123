a=input("введите натуральное число")
if not a.isdigit() or not a:
    print("ошибка")
else:
    max=0
    for x in a:
        e=int(x)
        if e>max:
            max=e
    print(f"наибольшая цифра {a}: {max}")