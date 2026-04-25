def operation_range(start, end, step, operator):
    numbers = list(range(start, end, step))
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/":
            result /= num
    return result
print(operation_range(1, 5, 1, "+"))
