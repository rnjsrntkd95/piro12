number = int(input())
bracket = []
tmp = ''
for i in range(number):
    bracket.append(input())
for target in bracket:
    stack = []
    target = list(target)
    for check in target:
        if check == '(':
            stack.append(check)
        else:
            if not stack:
                stack.append(check)
            else:
                tmp = stack.pop()
                if tmp != '(':
                    stack.append(tmp)
                    stack.append(check)
    if not stack:
        print('YES')
    else:
        print('NO')
