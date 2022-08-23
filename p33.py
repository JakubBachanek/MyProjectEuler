res = []

for i in range(10, 99):
    for j in range(i+1, 100):
        res_1 = i / j
        res_2 = 0

        d_1 = i % 10
        d_2 = (i//10) % 10

        d_3 = j % 10
        d_4 = (j//10) % 10

        if d_1 == 0 and d_3 == 0:
            continue

        if d_1 == d_3 and d_4 != 0:
            res_2 = d_2 / d_4
        elif d_1 == d_4 and d_3 != 0:
            res_2 = d_2 / d_3
        elif d_2 == d_3 and d_4 != 0:
            res_2 = d_1 / d_4
        elif d_2 == d_4 and d_3 != 0:
            res_2 = d_1 / d_3

        if res_2 > 0:
            if res_1 == res_2:
                res.append([i, j, res_1])


a = 1
b = 1
for i in res:
    a *= i[0]
    b *= i[1]


def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x


print(res)
temp = gcd(a, b)
print(a, b)
print(a//temp, b//temp)
