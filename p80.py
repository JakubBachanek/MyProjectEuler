MAX = 100

def sum_sqrt(n):
    p = 0
    t = []

    while n > 9:
        t.append(n % 100)
        n //= 100

    if n > 0:
        t.append(n)

    c = t[-1]
    t = t[:-1]
    root = []
    dig = 0

    while True:
        x = 0

        while True:
            if (x+1)*(20*p + (x+1)) > c:
                break

            x += 1

        root.append(x)
        dig += 1

        if dig == MAX:
            return sum(root)

        r = c - x*(20*p + x)
        p = 10*p + x

        if r == 0 and len(t) == 0:
            return 0

        if len(t) > 0:
            c = r*100 + t[-1]
            t = t[:-1]
        else:
            c = r*100


res = 0

for i in range(1, 101):
    res += sum_sqrt(i)


print(res)


