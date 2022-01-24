a = int(input("Enter integer: "))
b = a % 10
c = 0
while a > 0:
    if b > c:
        c=b
    a = a // 10
    b = a % 10
print('Maximum digit: ', c)
