LIMIT = 28123

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

for i in range(1, LIMIT):
    divs = find_proper_divisors(i)

    if sum(divs) > i:
        #print(i, divs)
        a_nums.append(i)

#print(a_nums)


a_sums = []
a_size = len(a_nums)

for i in range(a_size):
    for j in range(a_size):
        temp = a_nums[i] + a_nums[j]

        if temp < LIMIT:
            a_sums.append(temp)

#print(a_sums)
print(a_size)
print(len(a_sums))

a_sums = sorted(set(a_sums))
print(len(a_sums))

result = []

for i in range(1, LIMIT):
    if i not in a_sums:
        result.append(i)

print(sum(result))
