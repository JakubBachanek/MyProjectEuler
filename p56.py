result = 0

for i in range(1, 100):
    for j in range(1, 100):
        temp = i ** j
        sum = 0

        while temp > 0:
            sum += temp % 10
            temp //= 10

        if sum > result:
            result = sum

print(result)
