print("***************shoping system***************")
name=(input("enter customer name:"))
product =(input("enter product name:"))
price=int(input("enter product price:"))
qty=int(input("enter product qty:"))
t=price*qty
print("total amount:",t)

if t>=1500:
    di=t*.15
    print("total discount=",di)
elif t>=1000:
    di=t*.10
    print("total discount=",di)
elif t>=500:
    di=t*.5
    print("total discount=",di)
elif t<500:
    di=t*0
    print("total discount=",di)
ne=t-di
print("net price ",ne)
print("\t\tthank you for shoping")
