n = 1000
LIMIT = 100
MAX = 5000

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

primes[0], primes[1] = False, False

pr = [i for i in range(LIMIT+1) if primes[i]]

ways = [0 for _ in range(n+1)]
ways[0] = 1

for i in pr:
    for j in range(i, n+1):
        ways[j] += ways[j-i]

for i in range(len(ways)):
    if ways[i] > MAX:
        print(i, ways[i])
        break

