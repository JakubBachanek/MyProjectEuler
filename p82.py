SIZE = 80

data = ""

with open("p082_matrix.txt", "r") as file:
    data = file.read()
    data = data.split('\n')

t = list(data[:-1])

for i in range(len(t)):
    t[i] = t[i].split(",")

    for j in range(len(t[i])):
        t[i][j] = int(t[i][j])


for i in range(SIZE-1):
    a = []
    for j in range(SIZE):
        cur = t[SIZE-1-j][SIZE-1-i]

        temp = 0

        for k in range(j, SIZE-1):
            if (temp + t[SIZE-2-k][SIZE-1-i] + t[SIZE-2-k][SIZE-2-i]) < cur:
                cur = temp + t[SIZE-2-k][SIZE-1-i] + t[SIZE-2-k][SIZE-2-i]

            temp += t[SIZE-2-k][SIZE-2-i]

            if temp > cur:
                break

        temp = 0
        for k in range(j, 0, -1):
            if (temp + t[SIZE-k][SIZE-1-i] + t[SIZE-k][SIZE-2-i]) < cur:
                cur = temp + t[SIZE-k][SIZE-1-i] + t[SIZE-k][SIZE-2-i]

            temp += t[SIZE-k][SIZE-2-i]

            if temp > cur:
                break

        a.append(cur)

    for j in range(SIZE):
        t[SIZE-1-j][SIZE-2-i] += a[j]

m = t[0][0]

for i in range(SIZE):
    if t[i][0] < m:
        m = t[i][0]

print(m)

