import math
LIMIT = 10000

primes = [True for _ in range(LIMIT+1)]

p = 2

while p*p <= LIMIT:
    if primes[p] == True:
        for i in range(p*p, LIMIT+1, p):
            primes[i] = False

    p += 1


n = 9

while True:
    if primes[n]:
        n += 2
        continue

    able = False

    for i in range(n-2, 1, -2):
        if primes[i]:
            temp = math.sqrt((n-i) // 2)

            if temp - int(temp) == 0:
                able = True
                break

    if not able:
        print(n)
        break

    n += 2
