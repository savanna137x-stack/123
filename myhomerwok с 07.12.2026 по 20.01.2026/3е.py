word=input("введите слово:")
b={}
for letter in word:
    if letter in b:
        b[letter]+=1
    else:
        b[letter]=1
print("Количество букв в слове:")
print(b)

