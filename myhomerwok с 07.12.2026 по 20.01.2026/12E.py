def main(n):
    n+=1
    while str(n) == str(n)[::-1]:
        n+=1
    return n
print(main(11))
print(main(188))
print(main(2541))