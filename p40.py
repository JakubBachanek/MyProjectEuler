LIMIT = 1000000

d = ""
counter = 1
l = 1

while l <= LIMIT:
    s = str(counter)
    d += s
    l += len(s)
    counter += 1

result = 1
temp = 1

for i in range(7):
    result *= int(d[temp-1])
    temp *= 10

print(result)
