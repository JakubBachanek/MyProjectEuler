SIZE = 1001

n = [i for i in range(1, (SIZE)**2+1)]

c = 0
result = 1
temp = 2
c = 2

for i in range(SIZE // 2):
    for j in range(4):
        result += n[c+temp*j]

    c += 3*temp
    temp += 2
    c += temp

print(result)

