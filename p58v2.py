def check_prime(n):
    if n%2 == 0:
        return False

    prime = True
    p = 3

    while p*p < n+1:
        if n % p == 0:
            prime = False
            break

        p += 2

    return prime

result = 1
pr = 0
n = 3

while True:
    temp = n ** 2
    if check_prime(temp-n+1):
        pr += 1
    if check_prime(temp-2*n+2):
        pr += 1
    if check_prime(temp-3*n+3):
        pr += 1

    if pr / (n*2-1) < 0.1:
        print(pr / (n*2-1))
        result = n
        break

    n += 2

print(result)

