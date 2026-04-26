''''
a={'bomba':1,'kartoska':2,'art':3}
a["lopa"]=4
print(f"после добав :{a}")
'''''

''''''
a={'bomba':1,'kartoska':2,'art':3}
if "lopa" in a:
    print("правильно")
else:
    print("неправ")
''''''

''''''
a={'bomba':1,'kartoska':2,'art':3}
del a['art']

print("изменненый")