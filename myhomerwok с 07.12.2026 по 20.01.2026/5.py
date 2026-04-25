a=input("введите что то")
text =a
result = []

for char in text.lower():
    if char.isalpha():
        position = ord(char) - ord('a') + 1
        result.append(str(position))

print(" ".join(result))