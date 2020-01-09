a = int(input())


def divided_sum(a):
    d_sum, digit = a, 10
    while a // digit != 0:
        digit *= 10
    while True:
        b = a // digit
        d_sum += b
        a -= b * digit
        digit /= 10
        if digit == 1:
            d_sum += a
            return int(d_sum)


if a > 54:
    b = a - 54
else:
    b = 0

while True:
    c = divided_sum(b)
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
