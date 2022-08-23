d = []
s_digits = {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}
factorials = [1]

def generate(s, k, temp):
    if k == 0:
        d.append(temp)
        return

    for i in range(s, -1, -1):
        generate(i, k-1, temp*10+i)

generate(9, 7, 0)
d = d[:-1]

for i in range(1, 10):
    factorials.append(factorials[-1] * i)

memo = [0 for _ in range(9**2 * 7 + 1)]

for i in range(1, 9**2 * 7 + 1):
    k = i
    temp = 0

    while temp != 1 and temp != 89:
        temp = 0

        while k > 0:
            temp += s_digits[k % 10]
            k = k // 10
        k = temp

    memo[i] = temp


res = 0

for i in d:
    c = [0 for _ in range(10)]
    temp = str(i)
    test = 0

    for j in temp:
        c[int(j)] += 1
        test += s_digits[int(j)]

    if memo[test] != 89:
        continue

    value = factorials[7]

    for j in c:
        if j > 0:
            value //= factorials[j]

    res += value

print(res)
