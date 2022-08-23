LIMIT = 12000

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

r = 1 / 2
l = 1 / 3
n = 1
d = 3
res = 0
prev = 0

while True:
    if n/d >= r:
        d += 1
    else:
        n += 1

    a = (d % 2 == 0)

    if prev != d:
        t = n

        while t/d > l:
            if a and t % 2 == 0:
                t -= 1
                continue

            if t/d < r and gcd(t, d) == 1:
                res += 1

            t -= 1
    else:
        if n/d < r and n/d > l and gcd(n, d) == 1:
            res += 1

    if d == LIMIT:
        break

    prev = d

print(res)
