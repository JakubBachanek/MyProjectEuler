LIMIT = 1000000
MAX = 3000000
CHAIN_SIZE = 60

memo = [-1 for _ in range(MAX)]
fac = [1]
res = 0

for i in range(1, 10):
    fac.append(fac[-1]*i)

for i in range(1, LIMIT):
    chain = [i]
    c = 1
    temp = i
    found = False

    while True:
        s = str(temp)
        temp = 0

        for j in range(len(s)):
            temp += fac[int(s[j])]

        if memo[temp] != -1:
            c += memo[temp]

            if c == CHAIN_SIZE:
                res += 1

            for k in range(len(chain)):
                memo[chain[k]] = c
                c -= 1

            break

        for k in range(len(chain)):
            if chain[k] == temp:
                if c == CHAIN_SIZE:
                    res += 1

                for m in range(len(chain)):
                    if m < k:
                        memo[chain[m]] = c
                        c -= 1
                    else:
                        memo[chain[m]] = c

                found = True
                break

        if found:
            break

        chain.append(temp)
        c += 1


print(res)
