i = 100

while True:
    digits = list(str(i))
    digits.sort()
    found = True

    for j in range(2, 7):
        temp = i*j
        d = list(str(temp))
        d.sort()

        if digits != d:
            found = False
            break

    if found:
        print(i)
        break

    i += 1
