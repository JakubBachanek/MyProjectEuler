MAX = 10000000

memo = [0 for _ in range(MAX+1)]
s_digits = {0:0, 1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}


for i in range(1, MAX):
    if memo[i] > 0:
        continue

    temp = i
    chain = [i]

    while True:
        if memo[temp] > 0:
            for j in range(len(chain)):
                memo[chain[j]] = memo[temp]
            break

        s = str(temp)
        temp = 0

        for digit in s:
            temp += s_digits[int(digit)]

        if temp in chain:
            for j in range(len(chain)):
                memo[chain[j]] = temp
            break

        chain.append(temp)

res = 0

for i in memo:
    if i == 4:
        res += 1

print(res)
