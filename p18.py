LINES = 14

n = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")

new = []
for i in n:
    new.append(i.split())

test = [[[] for _ in range(0, i+1)] for i in range(LINES)]

for i in range(len(test)):
    for j in range(i+1):
        test[i][j].append(new[i+1][j])
        test[i][j].append(new[i+1][j+1])


sums = [75]
temp = [75]

for i in range(0, LINES):
    temp_cp = temp
    temp = []
    sums_new = []

    for j in range(len(sums)):
        cnt = 0

        for k in range(len(new[i])):
            if temp_cp[j] == int(new[i][k]):
                cnt = k
                break

        sums_new.append(sums[j] + int(test[i][cnt][0]))
        sums_new.append(sums[j] + int(test[i][cnt][1]))
        temp.append(int(test[i][cnt][0]))
        temp.append(int(test[i][cnt][1]))

    sums = sums_new

#print(sums)
print()
print(len(sums))
result = 0

for i in sums:
    if i > result:
        result = i

print(result)
