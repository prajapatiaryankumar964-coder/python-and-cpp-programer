n=int(input("enter the number:"))
t=0
for i in range(2,n):
    if(n%i==0):
        t=1
if(t==1):
    print("not prime value")
else:
    print("prime value")
