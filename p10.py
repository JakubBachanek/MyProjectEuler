LIMIT = 2000000

primes = [True for _ in range(LIMIT+1)]
sum = 0

p = 2

while p*p <= LIMIT:
    if primes[p] == True:
        for i in range(p*p, LIMIT+1, p):
            primes[i] = False

    p += 1


for i in range(2, LIMIT+1):
    if primes[i]:
        sum += i

print(sum)
