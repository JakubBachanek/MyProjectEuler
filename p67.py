LINES = 99

data = ""
with open("p067_triangle.txt", "r") as file:
    data = file.read().split("\n")

new = []
for i in data:
    new.append(i.split())


for i in range(len(new)):
    for j in range(len(new[i])):
        new[i][j] = int(new[i][j])

new_cp = new

for i in range(LINES):
    for j in range(len(new[LINES-i]) - 1):
        a = new_cp[LINES-i][j]
        b = new_cp[LINES-i][j+1]

        if a > b:
            new_cp[LINES-i-1][j] += a
        else:
            new_cp[LINES-i-1][j] += b

print(new_cp[0][0])
