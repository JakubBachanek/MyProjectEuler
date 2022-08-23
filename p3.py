NUM = 600851475143


max_prime = 2

while NUM % 2 == 0:
    NUM //= 2

i = 3

while i * i <= NUM:
    if NUM % i:
        i += 2
    else:
        NUM //= i
        max_prime = i

if NUM > 1:
    max_prime = NUM


print(max_prime)
