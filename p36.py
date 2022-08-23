LIMIT = 1000000

res = []

for i in range(LIMIT):
    s = str(i)
    l = len(s)

    pal = True

    for j in range(l // 2):
        if s[j] != s[l-j-1]:
            pal = False
            break

    if not pal:
        continue

    b = bin(i)[2:]
    l = len(b)

    for j in range(l // 2):
        if b[j] != b[l-j-1]:
            pal = False
            break

    if pal:
        res.append(i)


print(sum(res))
