def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

MAX = 50

res = 3 * MAX**2

for i in range(1, MAX+1):
    for j in range(1, MAX+1):
        f = gcd(i, j)

        a = j // f
        b = i // f

        x = (MAX - i) // a
        y = (j) // b

        if x > y:
            res += y
        else:
            res += x

        x = (MAX - j) // b
        y = (i) // a

        if x > y:
            res += y
        else:
            res += x


print(res)
