LIMIT = 1000000

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


result = 1

for i in range(3, LIMIT+1):
    if primes[i]:
        result += i-1
        continue

    factors = []

    while i % 2 == 0:
        i //= 2
        factors.append(2)

    t = 3

    while t * t <= i:
        if i % t:
            t += 2
        else:
            i //= t
            factors.append(t)

    if i > 1:
        factors.append(i)

    ctr = 0
    l = len(factors)
    unique_factors = []

    while True:
        k = 1
        a = factors[ctr]

        while ctr < l-1 and factors[ctr+1] == a:
            k += 1
            ctr += 1

        unique_factors.append([a, k])

        if ctr == l-1:
            break

        ctr += 1

    temp = 1

    for k in unique_factors:
        if k[1] > 1:
            temp *= (k[0]**(k[1]-1))*(k[0]-1)
        else:
            temp *= k[0]-1

    result += temp


print(result)
