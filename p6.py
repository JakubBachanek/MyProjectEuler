

sum_of_s = 0
sum = 0

for i in range(1, 101):
    sum_of_s += i ** 2
    sum += i

s_of_sum = sum ** 2

result = s_of_sum - sum_of_s

print(sum_of_s)
print(s_of_sum)
print(result)
