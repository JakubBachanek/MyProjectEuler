import math

MAX = 50000000
LIMIT = int(math.sqrt(MAX)+1)

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

primes[0] = False
primes[1] = False

primes = [i for i in range(2, len(primes)) if primes[i]]
l = len(primes)

i, j, k = 0, 0, 0
nums = set()

while True:
    a = primes[i]**4

    if a >= MAX:
        break

    while True:
        b = primes[j]**3

        if a+b >= MAX:
            break

        while True:
            if k > l-1:
                break

            c = primes[k]**2

            if a+b+c < MAX:
                nums.add(a+b+c)
            else:
                break

            k += 1
        j += 1
        k = 0
    i += 1
    j = 0
    k = 0


print(len(nums))
