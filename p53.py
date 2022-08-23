LIMIT = 100
MAX = 1000000
pascal_t = [0 for _ in range(LIMIT+1)]

pascal_t[0] = 1
counter = 0

for i in range(LIMIT):
    t = list(pascal_t)

    for j in range(1, LIMIT+1):
        pascal_t[j] += t[j-1]
        if pascal_t[j] > MAX:
            counter += 1

print(counter)


