LIMIT = 12000

def calcu(k):
    m = k // 6
    r = k % 6
    s = 0

    if r == 5:
        s = 1

    return m*(3*m + r - 2) + s

res = 0
fd2 = calcu(LIMIT // 2)
test = [1]

for j in range(6, LIMIT//3+1):
    temp = 0

    for m in range(2, j//5+1):
        temp += test[(j // m)-5]

    test.append(calcu(j) - temp)

res = calcu(LIMIT) - fd2
sum = 0

for m in range(3, LIMIT // 5+1, 2):
    sum += test[LIMIT // m - 5]


print(res - sum)
