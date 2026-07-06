cname = input("Enter customer name=")
pname = input("Enter product name=")

price=int(input("Enter price="))
qty=int(input("Enter quantity="))

gender=input("Enter gender(Male/Female)=")

total=price*qty
print("\nTotal=",total)

if total>=1500:
    dis=total*15/100
    print("Your discount 15%")

elif total>=1000:
    dis=total*10/100
    print("Your discount 10%")

elif total>=500:
    dis=total*5/100
    print("Your discount 5%")

else:
    dis=0
    print("No discount")

print("Discount=",dis)

net=total-dis
print("Net Price=", net)

print("\nThank You For Your Shopping Mr.",cname,"Good Luck")
