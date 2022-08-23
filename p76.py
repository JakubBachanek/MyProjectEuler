n = 100
coins = [i for i in range(1, n)]

ways = [0 for _ in range(n+1)]
ways[0] = 1

for i in coins:
    for j in range(i, n+1):
        ways[j] += ways[j-i]

print(ways[n])
