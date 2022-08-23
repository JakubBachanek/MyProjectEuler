def permute_pandigital(l):
    n = len(l)
    result = []
    c = [0 for _ in range(n)]
    result.append(list(l))
    i = 1

    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                l[0], l[i] = l[i], l[0]
            else:
                l[c[i]], l[i] = l[i], l[c[i]]

            if l[0] != 0:
                result.append(list(l))
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1

    return result


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

perms = permute_pandigital(digits)

divisors = [2, 3, 5, 7, 11, 13, 17]
result = 0

for p in perms:
    test = True
    s = ""
    for pp in p:
        s += str(pp)

    for i in range(len(divisors)):
        if int(s[1+i:4+i]) % divisors[i] != 0:
            test = False
            break

    if test:
        result += int(s)


print(result)
