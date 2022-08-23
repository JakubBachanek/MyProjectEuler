n = 110000


primes = [True for _ in range(n+1)]

p = 2

while p*p <= n:
    if primes[p] == True:
        for i in range(p*p, n+1, p):
            primes[i] = False

    p += 1



result = 0
counter = 0

for i in range(n+1):
    if primes[i]:
        counter += 1

        if counter == 10003:
            result = i
            break

print(result)

