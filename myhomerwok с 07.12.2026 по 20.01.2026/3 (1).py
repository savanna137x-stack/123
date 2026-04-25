a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
pervoe=a
vtoroe=b
while b:
    a, b = b, a % b
gcd = a

lcm = (pervoe * vtoroe) // gcd

print(f"Наименьшее общее кратное: {lcm}")
