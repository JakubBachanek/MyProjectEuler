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


class MinHeap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        newNode = [v, dist]

        return newNode

    def swapMinHeapNode(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp

    def minHeapify(self, index):
        smallest = index
        left = 2*index + 1
        right = 2*index + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        if smallest != index:
            self.pos[self.array[smallest][0]] = index
            self.pos[self.array[index][0]] = smallest
            self.swapMinHeapNode(smallest, index)
            self.minHeapify(smallest)


    def extractMin(self):
        if self.isEmpty():
            return

        root = self.array[0]

        last_node = self.array[self.size - 1]
        self.array[0] = last_node

        self.pos[last_node[0]] = 0
        self.pos[root[0]] = self.size - 1

        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        if self.size == 0:
            return True

        return False

    def decreaseKey(self, v, dist):
        index = self.pos[v]
        self.array[index][1] = dist

        while index > 0 and self.array[index][1] < self.array[(index-1) // 2][1]:
            self.pos[self.array[index][0]] = (index-1)//2
            self.pos[self.array[(index-1)//2][0]] = index
            self.swapMinHeapNode(index, (index-1)//2)
            index = (index-1)//2

    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True

        return False


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

heap = MinHeap()
heap.size = VERT_NUM

for i in range(VERT_NUM):
    heap.array.append(heap.newMinHeapNode(i, dist[i]))
    heap.pos.append(i)


while not heap.isEmpty():
    newNode = heap.extractMin()
    u = newNode[0]

    for vert in graph[u]:
        v = vert[0]

        if heap.isInMinHeap(v) and dist[u] != max and vert[1] + dist[u] < dist[v]:
            dist[v] = vert[1] + dist[u]
            heap.decreaseKey(v, dist[v])



print(dist[-1])
