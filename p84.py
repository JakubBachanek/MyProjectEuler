import random

ROLLS = 10000000
DICE_SIDES = 4

squares = [0 for _ in range(40)]

cc_pile = [i for i in range(16)]
ch_pile = [i for i in range(16)]

# Shuffle

for i in range(len(cc_pile)-1, -1, -1):
    j = random.randint(i, len(cc_pile)-1)
    temp = cc_pile[j]
    cc_pile[j] = cc_pile[i]
    cc_pile[i] = temp

for i in range(len(ch_pile)-1, -1, -1):
    j = random.randint(i, len(ch_pile)-1)
    temp = ch_pile[j]
    ch_pile[j] = ch_pile[i]
    ch_pile[i] = temp

current = 0
c_cc = 0
c_ch = 0
doubles_ctr = 0

for i in range(ROLLS):
    d_1 = random.randint(1, DICE_SIDES)
    d_2 = random.randint(1, DICE_SIDES)

    if d_1 == d_2:
        doubles_ctr += 1

        if doubles_ctr == 3:
            current = 10
            squares[current] += 1
            doubles_ctr = 0
            continue
    elif doubles_ctr > 0:
        doubles_ctr = 0

    next = (current + d_1 + d_2) % 40

    if next == 30:
        current = 10
        squares[current] += 1
    elif next == 2 or next == 17 or next == 33:
        if cc_pile[c_cc] == 0:
            current = 0
        elif cc_pile[c_cc] == 1:
            current = 10
        else:
            current = next

        squares[current] += 1
        c_cc += 1

        if c_cc == 16:
            c_cc = 0
    elif next == 7 or next == 22 or next == 36:
        if ch_pile[c_ch] == 0:
            current = 0
        elif ch_pile[c_ch] == 1:
            current = 10
        elif ch_pile[c_ch] == 2:
            current = 11
        elif ch_pile[c_ch] == 3:
            current = 24
        elif ch_pile[c_ch] == 4:
            current = 38
        elif ch_pile[c_ch] == 5:
            current = 5
        elif ch_pile[c_ch] == 6 or ch_pile[c_ch] == 7:
            if next == 7:
                current = 15
            elif next == 22:
                current = 25
            else:
                current = 5
        elif ch_pile[c_ch] == 8:
            if next == 7 or next == 36:
                current = 12
            elif next == 22:
                current = 28
        elif ch_pile[c_ch] == 9:
            if next == 36:
                if cc_pile[c_cc] == 0:
                    current = 0
                elif cc_pile[c_cc] == 1:
                    current = 10
                else:
                    current = next - 3

                squares[current] += 1
                c_cc += 1

                if c_cc == 16:
                    c_cc = 0
            else:
                current = next - 3
        else:
            current = next

        squares[current] += 1
        c_ch += 1

        if c_ch == 16:
            c_ch = 0

    else:
        current = next
        squares[current] += 1

test = [[squares[i] / ROLLS, i] for i in range(40)]
test.sort(reverse=True)
print(test[0][1], test[1][1], test[2][1])
