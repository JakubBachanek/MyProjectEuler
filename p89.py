data = ""

with open("p089_roman.txt", "r") as file:
    data = file.read()
    data = data.split('\n')

res = 0

for numeral in data:
    value = 0
    i = 0
    l = len(numeral)

    while i < l:
        n = numeral[i]

        if n == 'M':
            value += 1000
            i += 1
        elif n == 'D':
            value += 500
            i += 1
        elif n == 'C':
            if i+1 < l:
                if numeral[i+1] == 'M':
                    value += 900
                    i += 2
                    continue
                elif numeral[i+1] == 'D':
                    value += 400
                    i += 2
                    continue

            value += 100
            i += 1
        elif n == 'L':
            value += 50
            i += 1
        elif n == 'X':
            if i+1 < l:
                if numeral[i+1] == 'C':
                    value += 90
                    i += 2
                    continue
                elif numeral[i+1] == 'L':
                    value += 40
                    i += 2
                    continue

            value += 10
            i += 1
        elif n == 'V':
            value += 5
            i += 1
        elif n == 'I':
            if i+1 < l:
                if numeral[i+1] == 'X':
                    value += 9
                    i += 2
                    continue
                elif numeral[i+1] == 'V':
                    value += 4
                    i += 2
                    continue

            value += 1
            i += 1

#    temp = value
    rn = ""

    if value > 999:
        v = value // 1000
        rn += 'M' * v
        value = value % 1000

    if value > 99:
        v = value // 100

        if v < 4:
            rn += 'C' * v
        elif v == 4:
            rn += "CD"
        elif v == 9:
            rn += "CM"
        elif v > 4:
            rn += 'D'
            v -= 5

            if v > 0:
                rn += v * 'C'

        value = value % 100

    if value > 9:
        v = value // 10

        if v < 4:
            rn += 'X' * v
        elif v == 4:
            rn += "XL"
        elif v == 9:
            rn += "XC"
        elif v > 4:
            rn += 'L'
            v -= 5

            if v > 0:
                rn += v * 'X'

        value = value % 10

    if value > 0:
        if value < 4:
            rn += 'I' * value
        elif value == 4:
            rn += "IV"
        elif value == 9:
            rn += "IX"
        elif value > 4:
            rn += 'V'
            value -= 5

            if value > 0:
                rn += value * 'I'

    res += len(numeral)-len(rn)
#    print(numeral, " ", temp, " ", rn, len(numeral)-len(rn))
#    print()

print(res)
