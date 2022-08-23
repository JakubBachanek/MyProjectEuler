LIMIT = 1000000

x = [i for i in range(LIMIT+1)]

for i in range(2, LIMIT+1, 2):
    x[i] //= 2

p = 3

for i in range(p, LIMIT+1, 2):
    if x[i] == i:
        for j in range(i, LIMIT+1, i):
            x[j] *= (i-1)/i

print(int(sum(x))-1)
