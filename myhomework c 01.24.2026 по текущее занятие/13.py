def taxi(km,minparice=2,price1km=0.3):
    if km<=3:
        price=minparice
    else:
        pricekm=km -3
        price=minparice+pricekm*price1km
        return(price,2)
poezdka=taxi(km=17.5,minparice=2.0,price1km=0.3)
print(f"{poezdka}")