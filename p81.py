SIZE = 80

data = ""

with open("p081_matrix.txt", "r") as file:
    data = file.read()
    data = data.split('\n')

t = list(data[:-1])

for i in range(len(t)):
    t[i] = t[i].split(",")

    for j in range(len(t[i])):
        t[i][j] = int(t[i][j])


for i in range(SIZE-1):
    t[-1][SIZE-2-i] += t[-1][SIZE-1-i]

for i in range(SIZE - 1):
    t[-2-i][SIZE-1] += t[-1-i][SIZE-1]


for i in range(SIZE-1):
    for j in range(SIZE-1):
        if t[SIZE-2-i][SIZE-1-j] < t[SIZE-1-i][SIZE-2-j]:
            t[SIZE-2-i][SIZE-2-j] += t[SIZE-2-i][SIZE-1-j]
        else:
            t[SIZE-2-i][SIZE-2-j] += t[SIZE-1-i][SIZE-2-j]


print(t[0][0])
