import math

LIMIT = 1000000

c = 0
t = 2

while c < LIMIT:
    t += 1

    for i in range(3, 2*t + 1):
        s = math.sqrt(t**2 + i**2)

        if int(s) == s:
            if i <= t:
                c += i // 2
            else:
                c += 1 + (t - (i+1) // 2)

print(t)
