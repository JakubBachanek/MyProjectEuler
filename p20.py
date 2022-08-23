NUM = 100

result = 1
sum = 0

for i in range(2, NUM):
    result *= i

print(result)

for i in str(result):
    sum += int(i)

print(sum)
