MIN = 1010
MAX = 9999

tr = []
sq = []
pe = []
hexa = []
hept = []
oc = []

nums = [tr, sq, pe, hexa, hept, oc]
funs = [lambda n: (n*(n+1))//2, lambda n: n**2, lambda n: (n*(3*n-1))//2, lambda n: n*(2*n-1), lambda n: (n*(5*n-3))//2, lambda n: n*(3*n-2)]

for c in range(6):
    i = 1
    val = 0

    while True:
        val = funs[c](i)
        if val > MAX:
            break
        if val > MIN:
            nums[c].append(val)
        i += 1

l = len(nums)
cands = []

for c in range(len(nums)):
    for cc in range(c+1, len(nums)):
        for n in nums[c]:
            for nn in nums[cc]:
                if n % 100 == nn // 100:
                    cands.append([nn, n, cc, c])
                elif nn % 100 == n // 100:
                    cands.append([n, nn, c, cc])


for c in range(len(cands)):
    used = [False for _ in range(6)]
    used[cands[c][2]] = True
    used[cands[c][3]] = True

    for cc in range(l):
        if not used[cc]:
            s = [cands[c][0], 0, 0, 0, 0, cands[c][1]]
            for n in nums[cc]:
                if n // 100 == s[0] % 100:
                    s[1] = n
                    used[cc] = True

                    for ccc in range(l):
                        if not used[ccc]:
                            for nn in nums[ccc]:
                                if nn % 100 == s[5] // 100:
                                    s[4] = nn
                                    used[ccc] = True
                                    for cccc in range(l):
                                        if not used[cccc]:
                                            for nnn in nums[cccc]:
                                                if nnn // 100 == s[1] % 100:
                                                    s[2] = nnn
                                                    used[cccc] = True
                                                    for ccccc in range(l):
                                                        if not used[ccccc]:
                                                            for nnnn in nums[ccccc]:
                                                                if nnnn % 100 == s[4] // 100 and nnnn // 100 == s[2] % 100:
                                                                    s[3] = nnnn
                                                                    print(s, sum(s))
                                                                    print(cands[c][2], cc, ccc, cccc, ccccc, cands[c][3])
                                            used[cccc] = False
                            used[ccc] = False
            used[cc] = False
