a=int(input("ENTER YOUR VALUE FOR a="))
b=int(input("ENTER YOUR VALUE FOR b="))
c=int(input("ENTER YOUR VALUE FOR c="))
d=int(input("ENTER YOUR VALUE FOR d="))
e=int(input("ENTER YOUR VALUE FOR e="))

t=a+b+c+d+e
s=t/5
print("sum+",t)
print("average=",s)
if s>=90:
    print("you get a greade")
elif s>70:
    print("you get b grade")
elif s>50:
    print("you get c grade")
elif s<=35:
    print("you are fail")

