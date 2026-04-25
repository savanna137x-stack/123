def main(list1,list2):
    result=[]
    for a,b in zip(list1,list2):
        result.append(a+b)
    return result
print(main([1,2,3,],[4,5,6,]))