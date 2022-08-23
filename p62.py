LIMIT = 10000
res = []

for i in range(1, LIMIT):
    t = i**3
    d = []

    while t > 0:
        d.append(t%10)
        t //= 10

    res.append(d)

for i in range(len(res)):
    t = list(res[i])
    t.sort()
    c = 0

    for j in range(i+1, len(res)):
        if sorted(res[j]) == t:
            c += 1

        if c > 4:
            break

    if c == 4:
        print((i+1)**3)
        break
