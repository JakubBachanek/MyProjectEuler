

def prime_factors(n):
    i = 3
    factors = []
    while n % 2 == 0:
        n //= 2
        factors.append(2)

    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors

def prime_factorss(n):
    i = 3
    factors = set()
    while n % 2 == 0:
        n //= 2
        factors.add(2)

    while i * i <= n:
        if n % i:
            i += 2
        else:
            n //= i
            factors.add(i)

    if n > 1:
        factors.add(n)

    return factors

c = 2
f_1 = set()
f_2 = set()
f_3 = set()
f_1t = True
SIZE = 4

while True:
    if f_1t:
        f_1 = prime_factorss(c)

    f_2 = prime_factorss(c+1)

    temp = {s for s in f_1 if s not in f_2}

    if temp != f_1 or len(f_1) != SIZE or len(f_2) != SIZE:
        c += 1
        f_1t = False
        f_1 = f_2
        continue


    f_3 = prime_factorss(c+2)

    temp = {s for s in f_2 if s not in f_3}

    if temp != f_2 or len(f_3) != SIZE :
        c += 2
        f_1t = False
        f_1 = f_3
        continue

    f_4 = prime_factorss(c+3)

    temp = {s for s in f_3 if s not in f_4}

    if temp != f_3 or len(f_4) != SIZE :
        c += 3
        f_1t = False
        f_1 = f_4
        continue

    print(c, c+1, c+2, c+3, f_1, f_2, f_3, f_4)
    break
