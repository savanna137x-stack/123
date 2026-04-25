a=["Ари","GРОЛО"]
if a and all(x and x[0].isupper() for x in a):
    print("корректно")