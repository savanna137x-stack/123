def sign_text(n):
    if n > 0:
        return "Положительное"
    elif n < 0:
        return "Отрицательное"
    else:
        return "Ноль"
print(sign_text(5))