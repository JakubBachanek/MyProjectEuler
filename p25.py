MAX = 10 ** 999

fib = [1, 1]
temp = False
index = 2
num = 0

while num < MAX:
    index += 1
    num = fib[0] + fib[1]
    if temp:
        fib[1] = num
        temp = False
    else:
        fib[0] = num
        temp = True

print(num)
print(index)
