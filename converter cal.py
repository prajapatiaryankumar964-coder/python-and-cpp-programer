
v=float(input("Enter value:"))

print("\n(1) D to Rs.")
print("(2) Rs. to D")
print("(3) Cm. to Foot")
print("(4) Km to Foot")
print("(5) Pound to Kg")
print("(6) F to C")
print("(7) Exit")

ch=int(input("Enter your choice:"))

if ch==1:
    ans=v*96.02
    print("Ans=",ans)

elif ch==2:
    ans=v/96.02
    print("Ans=",ans)

elif ch==3:
    ans=v/30.48
    print("Ans=",ans)

elif ch==4:
    ans=v*3048
    print("Ans=",ans)

elif ch==5:
    ans=v*0.453592
    print("Ans=",ans)

elif ch==6:
    ans=(v-31)*5/9
    print("Ans=",ans)

elif ch==7:
    print("Program End")


else:
    print("Valid Choice")

