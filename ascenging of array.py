a=[]
n=int(input("how many elements ?:"))
print(n)
for i in range(n):
    b=int(input("enter value="))
    a.append(b)
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in range(n):
    print(a[i])
