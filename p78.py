p = [1]
res = 1

while True:
    c = 0
    temp = 1
    p.append(0)

    while temp <= res:
        sign = 1

        if c % 4 > 1:
            sign = -1

        p[res] += sign * p[res - temp]
        p[res] = p[res] % 1000000
        c += 1

        t = 0

        if c % 2 == 0:
            t = c // 2 + 1
        else:
            t = -(c // 2 + 1)

        temp = t * (3*t - 1) // 2

    if p[res] == 0:
        print(res)
        break

    res += 1
