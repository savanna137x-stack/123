text = input("Введите строку: ").lower()
vowels = "аейюёиоуэыя"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Количество гласных: {count}")