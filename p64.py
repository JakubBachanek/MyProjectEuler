LIMIT = 10000
import math

result = 0

for d in range(2, LIMIT+1):
    sd = math.sqrt(d)

    if sd - int(sd) == 0:
        continue

    a = int(sd)
    v = 1
    u = 0
    u = u + a*v
#    res = []
    l = 0
    temp = []
    found = False

    while True:
        v = (d - u**2) // v
        a = int((sd+u)//v)
        u = a*v-u

        for t in range(len(temp)):
            if [a, v, u] == temp[t]:
                if l % 2 == 1:
                    result += 1

                found = True
                break

        if found:
            break
#        res.append(a)
        l += 1
        temp.append([a, v, u])

print(result)
