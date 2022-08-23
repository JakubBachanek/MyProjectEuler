from itertools import combinations

points = []

for i in range(51):
    for j in range(51):
        points.append([i, j])

points = points[1:]
res = 0

for c in combinations(points, 2):
    p_0 = c[0]
    p_1 = c[1]

    a = c[0][0]**2 + c[0][1]**2
    b = c[1][0]**2 + c[1][1]**2
    c = (c[0][0] - c[1][0])**2 + (c[0][1] - c[1][1])**2

    temp = [a, b, c]

    if temp[0] > temp[1]:
        temp[0], temp[1] = temp[1], temp[0]

    if temp[1] > temp[2]:
        temp[1], temp[2] = temp[2], temp[1]

    if temp[0] + temp[1] == temp[2]:
        res += 1


print(res)
