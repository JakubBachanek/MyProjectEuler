import math
n = 144

while True:

    h = n*(2*n-1)
    temp = (1+math.sqrt(1+24*h)) / 6

    if temp - int(temp) > 0:
        n += 1
        continue

    print(h)
    break
