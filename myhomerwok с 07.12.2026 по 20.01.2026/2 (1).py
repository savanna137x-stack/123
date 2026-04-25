text = input("Введите строку: ").lower()
words = text.split()
count = 0
for word in words:
    if 'a' in word or 'а' in word:
        count += 1
print(f"Количество слов с буквой 'а': {count}")