def finaboc(n: int):
    a,b=1,1
    result=[]
    for x in range(n):
        result.append(str(a))
        a,b=b,a+b
    return "".join(result)
print(finaboc(7))

