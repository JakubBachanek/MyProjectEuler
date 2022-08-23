LIMIT = 1000
MAX = (LIMIT*LIMIT+LIMIT) * 2
primes = [True for _ in range(MAX+1)]
primes[0], primes[1] = False, False
p = 2

while p*p <= MAX:
    if primes[p] == True:
        for i in range(p*p, MAX+1, p):
            primes[i] = False

    p += 1

a = 0
b = 0
record = 0

for i in range(-LIMIT, LIMIT):
    for j in range(3, LIMIT, 2):
        if not primes[j]:
            continue

        n = 0

        while True:
            value = n*(i+n) + j

            if not primes[value]:
                if n > record:
                    record = n-1
                    a = i
                    b = j
                break

            n += 1


print(record, a, b, a*b)
