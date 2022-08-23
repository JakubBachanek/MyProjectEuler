digs_fac = [1]

temp = 1
for i in range(1, 10):
    temp *= i
    digs_fac.append(temp)

print(digs_fac)

MAX = digs_fac[9] * 7
res = []

for i in range(10, MAX):
    sum_fac = 0
    temp = [int(d) for d in str(i)]

    for j in temp:
        sum_fac += digs_fac[j]

    if sum_fac == i:
        res.append(i)


print()
print(res)
print(sum(res))
