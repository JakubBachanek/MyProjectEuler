LIMIT = 1500000
ways = [0 for _ in range(LIMIT+1)]

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

m = 2
n = 1

while 2*m*(m+1) <= LIMIT:
    while n < m:
        if (m+n) % 2 == 1 and gcd(m, n) == 1:
            temp = (m**2 - n**2) + (2*m*n) + (m**2 + n**2)

            for t in range(temp, LIMIT+1, temp):
                ways[t] += 1

        n += 1

    m += 1
    n = 1


res = 0

for i in range(LIMIT+1):
    if ways[i] == 1:
        res += 1

print(res)
