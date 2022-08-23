MAX = 97
r = 1

n = 1
d = 1

if MAX % 3 == 0:
    d = ((MAX//3)+1)*2

for i in range(MAX, 0, -1):
    if i % 3 == r:
        t = i // 3 + 1
        n = n + (2*t)*d
        n, d = d, n
    else:
        n = n + d
        n, d = d, n

n = n + d
n, d = d, n
n = n + 2*d

print(n, d)

res = 0

while n > 0:
    res += n % 10
    n //= 10

print(res)
