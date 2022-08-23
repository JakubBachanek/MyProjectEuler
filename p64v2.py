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
    l = 0
    found = False

    while True:
        v = (d - u**2) // v
        a = int((sd+u)//v)
        u = a*v-u

        if a == 2*int(sd):
            l += 1

            if l % 2 == 1:
                result += 1

            found = True
            break

        if found:
            break

        l += 1

print(result)
