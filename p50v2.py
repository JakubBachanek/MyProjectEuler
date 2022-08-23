LIMIT = 1000000
primes = [True for _ in range(LIMIT+1)]
primes_v = [2]
p = 2

while p*p <= LIMIT:
    if primes[p] == True:
        for i in range(p*p, LIMIT+1, p):
            primes[i] = False

    p += 1

p = 3

while p < LIMIT:
    if primes[p]:
        primes_v.append(p)
    p += 2

l = len(primes_v)
terms = 0
sum = 0

for i in range(l):
    c = 0
    s = 0

    for j in range(i, l):
        s += primes_v[j]

        if s > LIMIT:
            break

        c += 1

        if primes[s]:
            if c > terms:
                terms = c
                sum = s

print(sum)

