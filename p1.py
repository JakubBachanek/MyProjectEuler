MAX = 999

n = [False for i in range(0, MAX)]

temp_3 = 3
temp_5 = 5

while temp_3 <= MAX:
    n[temp_3 - 1] = True
    temp_3 += 3

while temp_5 <= MAX:
    n[temp_5 - 1] = True
    temp_5 += 5

counter = 1
sum = 0

while counter <= MAX:
    if n[counter - 1]:
        sum += counter

    counter += 1

print("Sum = " + str(sum))
