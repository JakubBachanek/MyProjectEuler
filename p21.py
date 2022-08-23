LIMIT = 10000

def find_proper_divisors(n):
    i = 2
    divs = [1]

    while i * i <= n:
        if n % i == 0:
            if n / i == i:
                divs.append(i)
            else:
                divs.append(n // i)
                divs.append(i)

        i += 1

    return divs

a_nums = []

for i in range(2, LIMIT):
    divs_1 = find_proper_divisors(i)
    sum_1 = sum(divs_1)

    divs_2 = find_proper_divisors(sum_1)
    sum_2 = sum(divs_2)

    if sum_2 == i and i != sum_1:
        a_nums.append(i)
        a_nums.append(sum_1)


result = sorted(set(a_nums))
print(result)
print(sum(result))
