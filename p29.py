a = 100
b = 100
result = []

for i in range(2, a+1):
    for j in range(2, b+1):
        value = i ** j
        result.append(value)

result = sorted(set(result))
print(result)
print(len(result))
