LIMIT = 12000

def find_partitions(min, n, prev):
    for d in range(min, n):
        if (n % d == 0 and n // d >= d):
            temp = prev + [d]
            glob.append(temp + [n // d])

            if (n // d > d):
                find_partitions(d, n // d, temp)


psn = [2*k for k in range(2*LIMIT)]

for i in range(2, 2*LIMIT + 1):
    glob = []
    find_partitions(2, i, [])

    for f in glob:
        prod = 1

        for k in f:
            prod *= k

        w = prod - sum(f) + len(f)

        if w <= LIMIT and psn[w] > prod:
            psn[w] = prod

psn = set(psn[2:LIMIT])
print(sum(psn))
