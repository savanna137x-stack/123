def check_prime():
    while True:
        user_input = input("Введите число  (или 'exit' для выхода): ")


        if user_input.lower() == "exit":
            print("Программа завершена")
            break


        if not user_input.isdigit():
            print("Ошибка Введите целое положительное число")
            continue

        num = int(user_input)

        if num < 2:
            print(f"Число {num} не является простым.")
            continue


        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"Число {num} — простое")
        else:
            print(f"Число {num} — составное")
        print("-" * 20)

check_prime()

