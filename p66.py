import math

LIMIT = 1000
result = [0, 0]

for d in range(2, LIMIT+1):
    if math.sqrt(d) == int(math.sqrt(d)):
        continue

    a = int(math.sqrt(d))+1
    b = 1
    k = a**2 - d*b**2

    if k == 1:
        a += 1
        k = a**2 - d*b**2

    while True:
        m = 1
        temp = 0
        first = False
        res_m = 0

        while True:
            if (a+b*m) % k == 0:
                if not first:
                    temp = abs(m**2 - d)
                    first = True
                    res_m = m
                else:
                    if abs(m**2 - d) < temp:
                        temp = abs(m**2 - d)
                        res_m = m
                    else:
                        break
            m += 1

        m = res_m
        t_1 = int((a*m+d*b) // k)
        t_2 = int((a+b*m) // k)
        t_3 = int((m**2 - d) // k)

        a, b, k = t_1, t_2, t_3

        if k == 1:
            if abs(a) > result[1]:
                result = [d, abs(a)]
            break

print(result)
