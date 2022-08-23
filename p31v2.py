n = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

ways = [0 for _ in range(201)]
ways[0] = 1

for i in coins:
    for j in range(i, 201):
        ways[j] += ways[j-i]

print(ways[200])
