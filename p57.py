MAX = 1000
a = 1
b = 2
result = 0

for i in range(MAX-1):
    d = b
    g = d*2 + a

    if len(str(g+d)) > len(str(g)):
        result += 1

    b = g
    a = d


print(result)
