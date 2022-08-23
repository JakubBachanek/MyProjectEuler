LIMIT = 1000000

primes = [True for _ in range(LIMIT+1)]

p = 2

while p*p <= LIMIT:
    if primes[p] == True:
        for i in range(p*p, LIMIT+1, p):
            primes[i] = False

    p += 1


counter = 1

for i in range(3, LIMIT, 2):
    if primes[i]:
        s = str(i)
        l = len(s)
        rot = []

        for j in range(l-1):
            rot.append(s[j+1:] + s[:j+1])

        rot_primes = True
        for r in rot:
            if not primes[int(r)]:
                rot_primes = False
                break

        if rot_primes:
            counter += 1


print(counter)
