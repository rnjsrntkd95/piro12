def dynamic(n):
    dp_dict = {1: 0, 2: 1, 3: 1}
    for up in range(4, n+1):
        check = 10000
        if up % 3 == 0:
            tmp = dp_dict[up // 3]
            if tmp < check:
                check = tmp
        if up % 2 == 0:
            tmp = dp_dict[up // 2]
            if tmp < check:
                check = tmp
        tmp = dp_dict[up - 1]
        if tmp < check:
            check = tmp
        dp_dict[up] = check + 1
    return dp_dict[n]

n = int(input())
print(dynamic(n))