def check_prime(n):
    if n == 1 or n%2 == 0:
        return False

    prime = True

    p = 3
    while p*p < n+1:
        if n % p == 0:
            prime = False
            break

        p += 2

    return prime


def permute(l):
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

            result.append(list(l))
            c[i] += 1
            i = 1
        else:
            c[i] = 0
            i += 1

    return result


res = 0

for i in range(1, 8):
    test = [i+1 for i in range(i)]
    perms = permute(test)

    for p in perms:
        n = 0

        for j in range(len(p)):
            n *= 10
            n += p[j]

        if check_prime(n):
            if n > res:
                res = n


print(res)











