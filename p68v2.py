import itertools
MAX = 10


t = [[] for _ in range(5, 20)]
res = []

for i in range(5, 20):
    a = 1
    b = i - a

    while a < i:
        if a <= MAX and b <= MAX and a != b:
            t[i-5].append([a, b])

        a += 1
        b -= 1


for i in range(len(t)):
    for j in range(len(t[i])):
        used = [False for _ in range(MAX)]
        temp = [[0, 0, 0] for _ in range(5)]

        temp[0][0], temp[0][1] = t[i][j][0], t[i][j][1]
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

            for u in range(len(copy)):
                if copy[u]:
                    continue

                sum = can[0][0] + can[0][1] + (u+1)
                can[0][2] = u+1
                can[1][1] = u+1
                test = sum - can[1][2]

                for kk in range(len(t[test-5])):
                    xx = t[test-5][kk][0]
                    yy = t[test-5][kk][1]

                    copy_n = list(copy)
                    copy_n[u] = True

                    if copy_n[xx-1] or copy_n[yy-1]:
                        continue

                    can_n = list(can)
                    copy_n[xx-1], copy_n[yy-1] = True, True

                    can_n[2][0] = xx
                    can_n[2][1] = can_n[1][2]
                    can_n[2][2] = yy
                    test_n = sum - can_n[2][2]

                    for kkk in range(len(t[test_n-5])):
                        xxx = t[test_n-5][kkk][0]
                        yyy = t[test_n-5][kkk][1]

                        if copy_n[xxx-1] or copy_n[yyy-1]:
                            continue

                        copy_nn = list(copy_n)
                        can_nn = list(can_n)
                        copy_nn[xxx-1], copy_nn[yyy-1] = True, True

                        can_nn[3][0] = xxx
                        can_nn[3][1] = can_nn[2][2]
                        can_nn[3][2] = yyy

                        test_nn = sum - can_nn[3][2] - can_nn[0][1]

                        if test_nn > 0 and test_nn < 10 and not copy_nn[test_nn-1]:
                            aa = int(str(can_nn[0][0]) + str(can_nn[0][1]) + str(can_nn[0][2]))
                            bb = int(str(can_nn[1][0]) + str(can_nn[1][1]) + str(can_nn[1][2]))
                            cc = int(str(can_nn[2][0]) + str(can_nn[2][1]) + str(can_nn[2][2]))
                            dd = int(str(can_nn[3][0]) + str(can_nn[3][1]) + str(can_nn[3][2]))
                            ee = int(str(test_nn) + str(can_nn[3][2]) + str(can_nn[0][1]))

                            aaa = can_nn[0][0]
                            bbb = can_nn[1][0]
                            ccc = can_nn[2][0]
                            ddd = can_nn[3][0]
                            eee = test_nn

                            if aaa < bbb and aaa < ccc and aaa < ddd and aaa < eee:
                                res.append([aa, bb, cc, dd, ee])
                            elif bbb < aaa and bbb < ccc and bbb < ddd and bbb < eee:
                                res.append([bb, cc, dd, ee, aa])
                            elif ccc < aaa and ccc < bbb and ccc < ddd and ccc < eee:
                                res.append([cc, dd, ee, aa, bb])
                            elif ddd < aaa and ddd < bbb and ddd < ccc and ddd < eee:
                                res.append([dd, ee, aa, bb, cc])
                            else:
                                res.append([ee, aa, bb, cc, dd])


res.sort()
res = list(aaa for aaa,_ in itertools.groupby(res))
result = 0

for r in res:
    temp = ""
    for s in r:
        temp += str(s)

    print(r, temp, len(temp))
    if len(temp) == 16 and int(temp) > result:
        result = int(temp)

print()
print(result)
