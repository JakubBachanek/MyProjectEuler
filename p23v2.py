LIMIT = 28123

def is_abundant(n):
    divs_sum = 1
    i = 2

    while i * i <= n:
        if n % i == 0:
            if n / i == i:
                divs_sum += i
            else:
                divs_sum += n // i
                divs_sum += i

            if divs_sum > n:
                return True

        i += 1

    return False


a_nums = []

for i in range(1, LIMIT):
    if is_abundant(i):
        a_nums.append(i)


a_sums = [False for _ in range(LIMIT)]
a_size = len(a_nums)

for i in range(a_size):
    for j in range(i, a_size):
        temp = a_nums[i] + a_nums[j]

        if temp < LIMIT:
            a_sums[temp] = True


result = 0

for i in range(LIMIT):
    if not a_sums[i]:
        result += i

print(result)
