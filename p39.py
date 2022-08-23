LIMIT = 1000

count = [0 for _ in range(LIMIT)]
temp = [i ** 2 for i in range(0, LIMIT)]

for p in range(12, LIMIT, 2):
    for a in range(1, p//3):
        b = (p*(p-2*a)) // (2*(p-a))

        if a > b:
            break

        c = p - a - b

        if temp[a] + temp[b] == temp[c]:
            count[p] += 1


res = 0

for i in count:
    if i > res:
        res = i

print(res)
