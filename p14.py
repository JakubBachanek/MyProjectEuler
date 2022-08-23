START_NUM = 1000000

def Collatz_seq(n):
    chain = []
    chain.append(n)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1

        chain.append(n)

    return chain

length = 0
current = 1
result = 0

for i in range(2, START_NUM):
#    print(i)
    c_seq = Collatz_seq(i)
    length = len(c_seq)
#    print(c_seq, length)

    if length > current:
        current = length
        result = i


print(result, current)
