MAX = 1000

def findit(d):
    n = 10
    rems = []
    result = 0
    digs = []

    while True:
        digit = n // d
        rem = n % d

        for j in range(len(rems)):
            if rems[j] == rem:
                rems = rems[j:]

                if digs[j] != digit:
                    digs = digs[j+1:]
                    digs.append(digit)

                result = len(rems)
                return result, digs

        rems.append(rem)
        digs.append(digit)
        n = rem * 10

        if n == 0:
            return 0, []



longest = 0
result = 0

for i in range(2, MAX):
    res, test = findit(i)

    if res > longest:
        longest = res
        result = i

print(longest, result)
