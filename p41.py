LIMIT = 10000000

def check_pandigital(n):
    s = str(n)
    l = len(s)
    comp = [i+1 for i in range(l)]
    st = [int(a) for a in s]

    if comp == sorted(st):
        return True

    return False


primes = [True for _ in range(LIMIT+1)]

p = 2

while p*p <= LIMIT:
    if primes[p] == True:
        for i in range(p*p, LIMIT+1, p):
            primes[i] = False

    p += 1


res = 0

for i in range(LIMIT+1):
    if primes[i]:
        if check_pandigital(i):
            if i > res:
                res = i


print(res)






