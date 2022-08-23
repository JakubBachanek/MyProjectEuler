LIMIT = 1000000

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

r = 3 / 7
n = 2
d = 5
res = []

while True:
    if n/d > r:
        d += 1
    else:
        n += 1

    if n/d < r and gcd(n, d) == 1:
        res = [n, d, n/d]

    if d == LIMIT:
        break

print(res)
