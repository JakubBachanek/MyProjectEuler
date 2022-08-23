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
sum = 0
c = 0
temp = []

while sum < LIMIT:
    sum += primes_v[c]
    c += 1

temp = [sum]

for i in range(l-c):
    temp.append(temp[-1] - primes_v[i] + primes_v[c+i])


found = False

while not found:
    value = temp[-1] - primes_v[-c]

    for i in range(len(temp)):
        if temp[i] < LIMIT and primes[temp[i]]:
            print(temp[i])
            found = True
            break

        temp[i] = temp[i] - primes_v[c+i-1]

    temp.append(value)
    c -= 1

