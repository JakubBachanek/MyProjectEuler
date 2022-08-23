NUM = 2000000
LIMIT = 100

x = 1
y = 1
current = [0, 0, 0]


while y < LIMIT:
    x = 1

    while x < LIMIT:
        c = int(x*(x+1)*y*(y+1) // 4)

        if abs(NUM-c) < abs(NUM-current[0]):
            current = [c, x, y]

        x += 1

    y += 1

print(current)
print(current[1]*current[2])
