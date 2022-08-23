LIMIT = 1000000000

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a



def generate_triples(max_len):
    n = 1
    m = 2

    while m**2 + 1 < max_len:
        if n >= m:
            n = m%2
            m += 1

        c = m**2 + n**2

        if c >= max_len:
            n = m
            continue

        if gcd(m, n) == 1:
            yield m**2 - n**2, 2*m*n, c

        n += 2



result = 0

# bruteforce
for a, b, c in generate_triples((LIMIT - 1) // 3):
    if abs(2*a - c) == 1:
        result += 2*a + 2*c
    elif abs(2*b - c) == 1:
        result += 2*b + 2*c


print(result)
