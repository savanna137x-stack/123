
def main(date):
    a=date.split('.')
    return f"{a[2]}-{a[1]}-{a[0]}"
print(main("01.03.2024"))
