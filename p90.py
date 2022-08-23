from itertools import combinations
from itertools import groupby

d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []

for c in combinations(d, 6):
    for cc in combinations(d, 6):
        s = {
            1 : False, 4 : False, 9 : False, 16 : False, 25 : False,
            36 : False, 49 : False, 64 : False, 81 : False
        }
        ss = [1, 4, 9, 16, 25, 36, 49, 64, 81]
        c_ext = list(c)
        cc_ext = list(cc)

        if 6 in c_ext and 9 not in c_ext:
            c_ext.append(9)
        elif 9 in c_ext and 6 not in c_ext:
            c_ext.append(6)

        if 6 in cc_ext and 9 not in cc_ext:
            cc_ext.append(9)
        elif 9 in cc_ext and 6 not in cc_ext:
            cc_ext.append(6)

        for a in c_ext:
            for b in cc_ext:
                temp = a*10 + b

                if temp in ss:
                    s[temp] = True

                temp = b*10 + a

                if temp in ss:
                    s[temp] = True

        flag = True

        for num in s:
            if not s[num]:
                flag = False
                break


        if flag:
            result.append([list(c), list(cc)])

result.sort()

res = list(result for result,_ in groupby(result))
print(len(res) // 2)
