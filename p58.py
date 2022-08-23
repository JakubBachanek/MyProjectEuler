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
temp = 2
pr = 0
n = 3

while True:
    for j in range(3):
        if check_prime(n+temp*j):
            pr += 1

    if pr / (temp*2+1) < 0.1:
        result = temp+1
        break

    n += 3*temp
    temp += 2
    n += temp

print(result)

