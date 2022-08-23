import math
n = 144

while True:
    h = n*(2*n-1)
    temp = math.sqrt(48*n*n - 24*n + 1)

    if temp - int(temp) > 0:
        n += 1
        continue

    k_1 = (1-6*n+temp) // 6
    t = n+k_1
    p = (t*(3*t-1)) // 2

    if h != p:
        n += 1
        continue

    print(h)
    break
