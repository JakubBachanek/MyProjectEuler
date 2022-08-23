LIMIT = 12000


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


b = 2
d = 3

k = 1
m = 1

res = 0

while True:
    if k*b + m*d > LIMIT:
        break

    while True:
        if k*b + m*d <= LIMIT:
            if gcd(k, m) == 1:
                res += 1
            m += 1
        else:
            break

    k += 1
    m = 1

print(res)
