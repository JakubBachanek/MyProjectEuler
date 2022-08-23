def check_prime(n):
    if n == 1:
        return False

    prime = True

    p = 3
    while p*p < n+1:
        if n % p == 0:
            prime = False
            break

        p += 2

    return prime


p = [1, 3, 7, 9]
temp = [2, 3, 5, 7]
a = []
for i in range(7):
    temp_2 = []
    for pp in temp:
        for j in range(4):
            if pp%10 != p[j]:
                temp_2.append(pp*10+p[j])
                a.append(pp*10+p[j])
    temp = temp_2

#print(temp)
print()
#print(a)
res = []

for i in a:
    s = str(i)
    l = len(s)

    l_r = []
    r_l = []
    pr = check_prime(i)
    if pr:
        test = True

        for j in range(l-1):
            part = int(s[j+1:])
            l_r.append(part)
            part_2 = int(s[:j+1])
            r_l.append(part_2)
            if not check_prime(part) or not check_prime(part_2):
                test = False
                break
        if test:
            res.append(i)
            print(i, l_r, r_l, pr)



print()
print(res)
print(sum(res))
