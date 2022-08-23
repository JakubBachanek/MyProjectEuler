data = ""

with open("p079_keylog.txt", "r") as file:
    data = file.read()
    data = data.split('\n')


res = []
test = [[[], []] for _ in range(10)]

for i in range(len(data)-1):
    temp = data[i]
    temp = [int(temp[0]), int(temp[1]), int(temp[2])]
    test[temp[1]][0].append(temp[0])
    test[temp[1]][1].append(temp[2])

for i in range(10):
    test[i][0] = list(set(test[i][0]))
    test[i][1] = list(set(test[i][1]))

iter = 0

while True:
    added = False

    for i in range(10):
        if len(test[i][0]) == 1:
            t = test[i][0][0]
            res.append(t)
            added = True

            for j in range(10):
                if t in test[j][0]:
                    test[j][0].remove(t)

    if not added:
        for i in range(10):
            if len(test[i][1]) == 1:
                res.append(i)
                res.append(test[i][1][0])
        break

temp = ""
for i in res:
    temp += str(i)
print(temp)
