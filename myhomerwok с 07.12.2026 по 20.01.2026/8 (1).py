a={"one":1,"two":99, (1,2):'tuple'}
print(f'clovar:{a}')

a["tree"]=120
print(f'clovar:{a}')

del a["tree"]
print(f'clovar:{a}')

b="{two}"
c=a.get('two')
print(f"получили '{b}':{c}")