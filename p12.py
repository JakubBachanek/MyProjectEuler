import math

DIVS_NUM = 500

def find_divisors(n):
    i = 1
    divs = []

    while i * i <= n:
        if n % i == 0:
            if n / i == i:
                divs.append(i)
            else:
                divs.append(n // i)
                divs.append(i)

        i += 1

    return divs

counter = 1
tr_nums = [1]


while True:
    temp_divs = find_divisors(tr_nums[-1])
    temp = len(temp_divs)

    if temp > DIVS_NUM:
        break

    counter += 1
    tr_nums.append(tr_nums[-1] + counter)


print(tr_nums[-1])
