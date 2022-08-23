res = 0
n = 1

while True:
    prev = res

    for i in range(9, 0, -1):
        temp = i ** n

        if len(str(temp)) == n:
            res += 1
        else:
            break

    if res == prev:
        break

    n += 1

print(res)
