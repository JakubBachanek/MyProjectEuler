LIMIT = 12000

(a, b, c, d) = (1, 3, 4000, LIMIT-1)
res = 1

while True:
    k = (LIMIT + b) // d
    (a, b, c, d) = (c, d, k * c - a, k * d - b)

    if c == 1 and d == 2:
        break

    res += 1

print(res)
