n=int(input("введитке что то"))
for x in range(1,n+1):
    for y in range(1, n+1):
        print(f"{x * y:2}", end="")
        print()