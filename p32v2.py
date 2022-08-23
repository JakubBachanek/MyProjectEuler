digits = [1,2,3,4,5,6,7,8,9]
res = []

def permute(l):
    n = len(l)
    result = []
    c = n * [0]

    result.append(list(l))

    i = 0;
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                tmp = l[0]
                l[0] = l[i]
                l[i] = tmp

            else:

                tmp = l[c[i]]
                l[c[i]] = l[i]
                l[i] = tmp

            result.append(list(l))
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return result


perm_d = permute(digits)

for i in range(1, 3):
    j = 5-i

    for k in perm_d:
        num_1 = 0
        num_2 = 0
        product = 0


        for t in range(0, i):
            num_1 = num_1*10 + k[t]

        for t in range(i, i+j):
            num_2 = num_2*10 + k[t]

        for t in range(i+j, 9):
            product = product*10 + k[t]

        if num_1*num_2 == product:
            res.append(product)


res = set(res)
print(res)
print(sum(res))
