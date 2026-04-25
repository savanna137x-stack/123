a=input("введите последовательность чисел")
a.split(',')
b_spisok=[]
for i in a:
    clean=i.strip()
    b=int(clean)
    b_spisok.append(b)
print("ваш список чисел:",b_spisok)
