n = 2 ** 1000

digits = str(n)
result = 0

for i in digits:
    result += int(i)

print(result)
