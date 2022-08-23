SIZE = 20

def count_paths():
    grid = [[1 for _ in range(SIZE)] for _ in range(SIZE)]

    for i in range(SIZE):
        for j in range(SIZE):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    print(grid[SIZE-1][SIZE-1])

count_paths()
