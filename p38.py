def check_pandigital(n):
    temp = [False for _ in range(9)]

    while n > 0:
        d = n % 10
        n = n // 10
        if d > 0:
            temp[d-1] = True

    for i in temp:
        if not i:
            return False

    return True

result = 0

for i in range(1, 10000):
    num = ""
    temp = 0
    test = False

    for j in range(1, 10):
        num += str(i*j)
        l = len(num)

        if l < 9:
            continue
        else:
            if l == 9:
                temp = int(num)
                if check_pandigital(temp):
                    test = True
            break

    if test:
        if temp > result:
            result = temp


print(result)
