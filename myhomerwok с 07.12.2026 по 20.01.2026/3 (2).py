score=int(input("введите оценку"))
if score<0 or score>100:
    print("ошибка")
elif score>=90:
    print("отличник")
elif score>=50:
    print("хорошист")
else:

    print("оценка не удов")