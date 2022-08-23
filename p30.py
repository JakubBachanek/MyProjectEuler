LIMIT = (9**5)*7
sum = 0

for i in range(10, LIMIT):
    value = 0
    temp = str(i)
    for j in temp:
        value += int(j) ** 5

    if value == i:
        sum += value

print(sum)
