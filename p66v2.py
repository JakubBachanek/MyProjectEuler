LIMIT = 1000
res = [0, 0]

for n in range(2, LIMIT+1):
    n1, d1 = 0, 1
    n2, d2 = 1, 0

    while True:
        a = n1+n2
        b = d1+d2

        t = a*a - n*b*b

        if t == 1:
            if res[0] < a:
                res = [a, n]
            break
        elif t == 0:
            break
        else:
            if t > 0:
                n2 = a
                d2 = b
            else:
                n1 = a
                d1 = b

print(res)
