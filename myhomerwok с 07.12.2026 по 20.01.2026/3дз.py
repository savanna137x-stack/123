a=input("ввдите натурлаьное число")
if not a.isdigit() or not a:
    priny("введино не натуральное число")
else:
    max=0
    for x in a:
        e=int(x)
        if e>max:
            max=e
            print(max)