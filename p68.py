import itertools
MAX = 6

t = [[] for _ in range(5, 13)]
res = []

for i in range(5, 13):
    a = 1
    b = i - a

    while a < i:
        if a <= MAX and b <= MAX and a != b:
            t[i-5].append([a, b])

        a += 1
        b -= 1


for i in range(len(t)):
    for j in range(len(t[i])):
        used = [False for _ in range(6)]
        temp = [[0, 0, 0] for _ in range(3)]

        temp[0][0], temp[0][1] = t[i][j][0], t[i][j][1]
#        print("UST TU: ", temp[0][0], temp[0][1])
        used[temp[0][0]-1] = True
        used[temp[0][1]-1] = True

        for k in range(len(t[i])):
            x = t[i][k][0]
            y = t[i][k][1]

            if used[x-1] or used[y-1]:
                continue

            copy = list(used)
            can = list(temp)
            copy[x-1], copy[y-1] = True, True

            can[1][0] = x
            can[1][2] = y

            for kk in range(len(copy)):
                if not copy[kk]:
                    sum = can[0][1] + can[1][2] + (kk+1)
                    test = sum - can[0][0] - can[0][1]


                    if test > 0 and test < 7 and not copy[test-1]:

                        aa = 100*can[0][0] + 10*can[0][1] + test
                        bb = 100*can[1][0] + 10*test + can[1][2]
                        cc = 100*(kk+1) + 10*can[1][2] + can[0][1]

                        if aa < bb and aa < cc:
                            res.append([aa, bb, cc])
                        elif bb < aa and bb < cc:
                            res.append([bb, cc, aa])
                        else:
                            res.append([cc, aa, bb])

#                        print("GOOD: ", sorted([[can[0][0], can[0][1], test], [can[1][0], test, can[1][2]], [kk+1, can[1][2], can[0][1]]]))
#                        res.append(sorted([[can[0][0], can[0][1], test], [can[1][0], test, can[1][2]], [kk+1, can[1][2], can[0][1]]]))

res.sort()
res = list(aaa for aaa,_ in itertools.groupby(res))

for r in res:
    print(r)
