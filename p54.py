data = ""

with open("p054_poker.txt", "r") as file:
    data = file.read()

data = data.split("\n")

def check_royal_flush(h):
    correct = [10, 11, 12, 13, 14]
    suit = h[0][1]
    temp = []
    test = True

    for card in h:
        if card[1] != suit:
            test = False
            break

        temp.append(card[0])

    if not test:
        return False

    temp.sort()

    if temp == correct:
        return True

    return False

def check_straight_flush(h):
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suit = h[0][1]
    temp = []
    test = True

    for card in h:
        if card[1] != suit:
            test = False
            break

        temp.append(card[0])

    if not test:
        return [False, False]

    test = False
    temp.sort()

    for c in range(9):
        if temp == values[c:c+5]:
            test = True
            break

    if test:
        return [True, temp[-1]]

    return [False, False]


def check_four_of_a_kind(h):
    val, c_1 = h[0][0], 1
    val_2, c_2 = -1, 0
    test = True

    for c in range(1, 5):
        if h[c][0] == val:
            c_1 += 1
        else:
            if val_2 == -1:
                val_2 = h[c][0]
                c_2 += 1
                continue
            elif val_2 == h[c][0]:
                c_2 += 1
            else:
                test = False
                break

    if not test:
        return [False, False]
    elif c_1 == 4:
        return [True, h[c][0]]
    elif c_2 == 4:
        return [True, val_2]

    return [False, False]

def check_full_house(h):
    a = [h[0][0]]
    b = []
    test = True

    for c in range(4):
        if h[c+1][0] == a[0]:
            a.append(h[c+1][0])
        else:
            b.append(h[c+1][0])

    if len(a) == 2:
        t = b[0]

        for c in range(2):
            if b[c+1] != t:
                test = False
                break
    elif len(a) == 3:
        if b[0] != b[1]:
            test = False
    else:
        test = False

    if test:
        t = [-1, -1]
        if len(a) == 2:
            t[0], t[1] = b[0], a[0]
        else:
            t[0], t[1] = a[0], b[0]

        return [True, t]

    return [False, False]


def check_flush(h):
    suit = h[0][1]
    test = True

    for c in range(4):
        if suit != h[c+1][1]:
            test = False
            break

    if test:
        return True

    return False


def check_straight(h):
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    temp = [card[0] for card in h]
    test = False
    temp.sort()

    for c in range(9):
        if temp == values[c:c+5]:
            test = True
            break

    if test:
        return [True, temp[-1]]

    return [False, False]


def check_three_of_a_kind(h):
    temp = [card[0] for card in h]
    temp.sort()
    t = temp[0]
    c = 1
    counter = 1
    test = False

    while c < 5:
        if temp[c] == t:
            counter += 1
        else:
            t = temp[c]
            counter = 1

        if counter == 3:
            test = True
            break

        c += 1

    if test:
        return [True, t]

    return [False, False]

def check_two_pairs(h):
    temp = [card[0] for card in h]
    temp.sort()

    if temp[0] == temp[1] and temp[2] == temp[3]:
        if temp[0] > temp[2]:
            return [True, temp[0], temp[2]]
        else:
            return [True, temp[2], temp[0]]
    elif temp[1] == temp[2] and temp[3] == temp[4]:
        if temp[1] > temp[3]:
            return [True, temp[1], temp[3]]
        else:
            return [True, temp[3], temp[1]]
    elif temp[0] == temp[1] and temp[3] == temp[4]:
        if temp[0] > temp[3]:
            return [True, temp[0], temp[3]]
        else:
            return [True, temp[3], temp[0]]

    return [False, False, False]

def check_one_pair(h):
    temp = [card[0] for card in h]
    temp.sort()

    for c in range(4):
        if temp[c] == temp[c+1]:
            return [True, temp[c]]

    return [False, False]

def check_high_card(h):
    highest = 0

    for t in h:
        if t > highest:
            highest = t

    return highest

checks = [check_royal_flush, check_straight_flush, check_four_of_a_kind, check_full_house, check_flush, check_straight, check_three_of_a_kind, check_two_pairs, check_one_pair]

def compare_hands(h_1, h_2):
    a = [[h_1[0+t*3], h_1[1+t*3]] for t in range(0, 5)]
    b = [[h_2[0+t*3], h_2[1+t*3]] for t in range(0, 5)]

    for c in range(5):
        if a[c][0] == "T":
            a[c][0] = 10
        elif a[c][0] == "J":
            a[c][0] = 11
        elif a[c][0] == "Q":
            a[c][0] = 12
        elif a[c][0] == "K":
            a[c][0] = 13
        elif a[c][0] == "A":
            a[c][0] = 14
        else:
            a[c][0] = int(a[c][0])

        if b[c][0] == "T":
            b[c][0] = 10
        elif b[c][0] == "J":
            b[c][0] = 11
        elif b[c][0] == "Q":
            b[c][0] = 12
        elif b[c][0] == "K":
            b[c][0] = 13
        elif b[c][0] == "A":
            b[c][0] = 14
        else:
            b[c][0] = int(b[c][0])


    c = 0
    a_c = 10
    b_c = 10
    a_t = -1
    b_t = -1
    flag_1 = True
    flag_2 = False

    for c in range(9):
        if c in [1, 2, 3, 5, 6, 7, 8]:
            temp = checks[c](a)

            if temp[0]:
                a_c = c
                a_t = temp[1]
                flag_1 = True
                break
        else:
            if checks[c](a):
                a_c = c
                break

    for c in range(9):
        if c in [1, 2, 3, 5, 6, 7, 8]:
            temp = checks[c](b)

            if temp[0]:
                b_c = c
                b_t = temp[1]
                flag_2 = True
                break
        else:
            if checks[c](b):
                b_c = c
                break


    if a_c == 10 and b_c == 10:
        temp_a = [card[0] for card in a]
        temp_b = [card[0] for card in b]

        for c in range(5):
            t_1 = check_high_card(temp_a[:5-c])
            t_2 = check_high_card(temp_b[:5-c])

            if t_1 == t_2:
                continue
            elif t_1 > t_2:
                return 0
            else:
                return 1


    if a_c == b_c:
        if flag_1 and flag_2:
            if a_c == 3:
                if a_t[0] == b_t[0]:
                    if a_t[1] == b_t[1]:
                        temp_a = [card[0] for card in a]
                        temp_b = [card[0] for card in b]

                        for c in range(5):
                            t_1 = check_high_card(temp_a[:5-c])
                            t_2 = check_high_card(temp_b[:5-c])

                            if t_1 == t_2:
                                continue
                            elif t_1 > t_2:
                                return 0
                            else:
                                return 1
                    elif a_t[1] > b_t[1]:
                        return 0
                    else:
                        return 1
                elif a_t[0] > b_t[0]:
                    return 0
                else:
                    return 1
            elif a_c == 7:
                if a_t[1] == b_t[1]:
                    if a_t[2] == b_t[2]:
                        temp_a = [card[0] for card in a]
                        temp_b = [card[0] for card in b]

                        for c in range(5):
                            t_1 = check_high_card(temp_a[:5-c])
                            t_2 = check_high_card(temp_b[:5-c])

                            if t_1 == t_2:
                                continue
                            elif t_1 > t_2:
                                return 0
                            else:
                                return 1
                    elif a_t[2] > b_t[2]:
                        return 0
                    else:
                        return 1
                elif a_t[1] > b_t[1]:
                    return 0
                else:
                    return 1
            else:
                if a_t == b_t:
                    temp_a = [card[0] for card in a]
                    temp_b = [card[0] for card in b]

                    for c in range(5):
                        t_1 = check_high_card(temp_a[:5-c])
                        t_2 = check_high_card(temp_b[:5-c])

                        if t_1 == t_2:
                            continue
                        elif t_1 > t_2:
                            return 0
                        else:
                            return 1
                elif a_t > b_t:
                    return 0
                else:
                    return 1

    elif a_c < b_c:
        return 0
    else:
        return 1

result = 0

for i in range(len(data)-1):
    game = data[i]
    hand_1 = game[:14]
    hand_2 = game[15:]
    temp = compare_hands(hand_1, hand_2)

    if temp == 0:
        result += 1


print(result)
