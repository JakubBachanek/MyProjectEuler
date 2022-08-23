SIZE = 80
VERT_NUM = SIZE**2

data = ""

with open("p083_matrix.txt", "r") as file:
    data = file.read()
    data = data.split('\n')

t = list(data[:-1])

for i in range(len(t)):
    t[i] = t[i].split(",")

    for j in range(len(t[i])):
        t[i][j] = int(t[i][j])



graph = []

for i in range(SIZE):
    for j in range(SIZE):
        graph.append([])

        if i == 0:
            graph[-1].append([(SIZE*(i+1)+j), t[i+1][j]])
        elif i == SIZE-1:
            graph[-1].append([(SIZE*(i-1)+j), t[i-1][j]])
        else:
            graph[-1].append([(SIZE*(i+1)+j), t[i+1][j]])
            graph[-1].append([(SIZE*(i-1)+j), t[i-1][j]])

        if j == 0:
            graph[-1].append([(SIZE*i+j+1), t[i][j+1]])
        elif j == SIZE-1:
            graph[-1].append([(SIZE*i+j-1), t[i][j-1]])
        else:
            graph[-1].append([(SIZE*i+j+1), t[i][j+1]])
            graph[-1].append([(SIZE*i+j-1), t[i][j-1]])

max = 2**19
dist = [max for _ in range(VERT_NUM)]
dist[0] = t[0][0]
finished = [False for _ in range(VERT_NUM)]

def min_dist(dist, fin):
    min = max
    index = 0

    for u in range(VERT_NUM):
        if dist[u] < min and not fin[u]:
            min = dist[u]
            index = u

    return index

for a in range(VERT_NUM):
    x = min_dist(dist, finished)
    finished[x] = True

    for vert in graph[x]:
        if not finished[vert[0]] and (dist[x] + vert[1]) < dist[vert[0]]:
            dist[vert[0]] = dist[x] + vert[1]

print(dist[-1])
