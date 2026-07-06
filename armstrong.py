
n = int(input("Enter Number: "))

temp = n
s = 0

while n > 0:
    d = n % 10
    s = s + (d ** 3)
    n = n // 10

print("Armstrong Value =", s)

if temp == s:
    print(temp, "is Armstrong Number")
else:
    print(temp, "is Not Armstrong Number")



print("Armstrong Numbers from 1 to 1000:")

for num in range(1, 1001):
    temp = num
    s = 0

    while temp > 0:
        d = temp % 10
        s = s + (d ** 3)
        temp = temp // 10

    if s == num:
        print(num, end=" ")
