MAX = 4000000


fib = [0, 1]
sum = 0

while fib[-1] <= MAX:
    if fib[-1] % 2 == 0:
        sum += fib[-1]

    fib.append(fib[-1] + fib[-2])


print(fib)
print("Sum = " + str(sum))
