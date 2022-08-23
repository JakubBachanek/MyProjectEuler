MAX = 1000000
LIMIT = 20

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

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

n = 2
c = 3

while True:
    if primes[c]:
        if n * c > MAX:
            break

        n = n*c

    c += 2

c = 1
a = 2

while a < n:
    if gcd(a, n) == 1:
        c += 1

    a += 1

print(n, n/c)
