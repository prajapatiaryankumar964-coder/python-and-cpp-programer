n=int(input("enter the number:"))
t=0
i=2
while i<n:
    
    if(n%i==0):
        t=1
    i=i+1
if(t==1):
    print("not prime value")
else:
    print("prime value")
