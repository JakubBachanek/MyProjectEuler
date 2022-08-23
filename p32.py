res = []
digits = [1,2,3,4,5,6,7,8,9]
d_l = len(digits)

def gen_comb(temp, data, d, s, start, end, index):

    if index == s:
        temp.append([data[j] for j in range(len(data))])
        return

    i = start

    while i <= end and end-i+1 >= s - index:
        data[index] = d[i]
        gen_comb(temp, data, d, s, i+1, end, index+1)
        i += 1

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


def check_product(digs, prod):
    prod_str = str(prod)
    prod_str = [int(dig) for dig in prod_str]

    if sorted(digs) == sorted(prod_str):
        res.append(prod)


for i in range(1, 3):
    temp = []
    comb = [0 for _ in range(i)]
    gen_comb(temp, comb, digits, i, 0, d_l-1, 0)
    perms = [permute(a) for a in temp]
    min = 5 - i
    max = 5-i + 1

    for j in range(min, max):
        temp_2 = []

        for k in range(len(temp)):
            temp_2 = []
            num_2_d = [d for d in digits if d not in temp[k]]
            comb_2 = [0 for _ in range(j)]
            gen_comb(temp_2, comb_2, num_2_d, j, 0, len(num_2_d)-1, 0)
            perms_2 = [permute(c) for c in temp_2]

            for p in perms[k]:
                num_1 = ""

                for digit in p:
                    num_1 += str(digit)
                num_1 = int(num_1)

                for pp in perms_2:
                    for per in pp:
                        num_2 = ""

                        for digit in per:
                            num_2 += str(digit)

                        num_2 = int(num_2)
                        product = num_1 * num_2
                        product_d = [d for d in digits if d not in temp[k] and d not in per]
                        check_product(product_d, product)


res = set(res)
print(res)
print(sum(res))
