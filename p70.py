import math
LIMIT = 10000000

primes = [True for _ in range(LIMIT+1)]
p = 2

for i in range(p*p, LIMIT+1, p):
    primes[i] = False

p = 3

while p*p <= LIMIT:
    if primes[p] == True:
        for i in range(p*p, LIMIT+1, p):
            primes[i] = False

    p += 2

res = [0, 10]

for i in range(997, LIMIT, 2):
    if not primes[i]:
        continue

    if i * (i+2) > LIMIT:
        break

    for j in range(i+2, LIMIT, 2):
        if not primes[j]:
            continue

        temp = i*j

        if temp > LIMIT:
            break

        t = (i-1)*(j-1)

        c1 = temp
        c2 = t

        d_1 = []
        d_2 = []

        while c1 > 0:
            d_1.append(c1%10)
            c1 //= 10

        while c2 > 0:
            d_2.append(c2%10)
            c2 //= 10

        d_1.sort()
        d_2.sort()

        if d_1 == d_2:
            if temp / t < res[1]:
                res = [temp, temp / t]

print(res)
