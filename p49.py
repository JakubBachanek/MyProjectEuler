from itertools import combinations
LIMIT = 10000

def permute(l):
    n = len(l)
    result = []
    c = [0 for _ in range(n)]
    result.append(list(l))
    i = 1

    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                l[0], l[i] = l[i], l[0]
            else:
                l[c[i]], l[i] = l[i], l[c[i]]

            result.append(list(l))
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1

    return result

primes = [True for _ in range(LIMIT+1)]

p = 2

while p*p <= LIMIT:
    if primes[p] == True:
        for i in range(p*p, LIMIT+1, p):
            primes[i] = False

    p += 1

found = False

for i in range(1001, 10000):
    if primes[i] and i != 1487:
        s = str(i)
        digits = [d for d in s]
        perm = permute(digits)

        for j in perm:
            l = len(j)
            num = ""
            for d in range(l):
                num += j[d]

            num = int(num)
            if primes[num] and num > i:
                dif = num - i
                next = num + dif

                if next < 10000 and primes[next]:
                    next_s = str(next)
                    temp = [ss for ss in next_s]
                    if temp in perm:
                        found = True
                        print(str(i)+str(i+dif)+str(i+2*dif))
                        break

        if found:
            break
