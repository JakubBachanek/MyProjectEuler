from itertools import combinations
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


i = 1009
found = False
l = 3

while not found:
    if not primes[i]:
        i += 2
        continue

    s = str(i)
    l = len(s)
    pool = [d for d in range(l-1)]

    for n in range(3, l):
        combs = list(combinations(pool, n))

        for j in range(len(combs)):
            cnt = 0
            result = []

            for c in range(0, 10):
                if c == 0 and c in combs[j]:
                    continue

                temp = list(s)
                sub = str(c)

                for d in combs[j]:
                    temp[d] = sub

                temp = int("".join(temp))

                if primes[temp]:
                    cnt += 1
                    result.append(temp)

                if cnt - c == -3:
                    break

            if cnt == 8:
                print(result)
                found = True
                break

        if found:
            break

    i += 2
