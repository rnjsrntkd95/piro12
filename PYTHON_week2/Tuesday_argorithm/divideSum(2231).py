a = int(input())

def dividedSum (a):
    sum, digit = a, 10
    while a // digit != 0:
        digit *= 10
    while True:
        b = a // digit
        sum += b
        a -= b * digit
        digit /= 10
        if(digit == 1):
            sum += a
            return int(sum)
if a > 54:
    b = a - 54
else:
    b = 0

while True:
    c = dividedSum(b)
    if b == c:
        print(0)
        break
    elif c == a:
        print(b)
        break
    b += 1
    if b == a:
        print(0)
        break