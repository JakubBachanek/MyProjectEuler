#1,2,3,4,5,6,7,8,9,10

#2,3,5,7,

#1 2 3 [2 2] 5 [3 3] 7 [2 2 2] [3 3] [2 5]


#2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20


#2 3 [2 2] 5 [3 3] 7 [2 2 2] [3 3] [2 5] 11 [2 2 3] 13 [2 7] [3 5] [2 2 2 2] 17 [2 3 3] 19 [2 2 5]

from collections import Counter
import math

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)
    return factors


fac_result = []

for i in range(0, 21):
    temp = prime_factors(i)
    rem = Counter(fac_result)

    out = []
    for val in temp:
        if rem[val]:
            rem[val] -= 1
        else:
            out.append(val)
    fac_result.extend(out)

fac_result.sort()
print(fac_result)
print(math.prod(fac_result))
