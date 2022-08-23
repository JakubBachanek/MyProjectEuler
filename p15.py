SIZE = 15
END = [0, 0]
paths_num = 0

def run_paths(grid):
    go_right(grid)
    go_down(grid)

def go_right(grid):
    global paths_num
#    print("IDE PRAWO")
    grid = [grid[0], grid[1]-1]
#    print(grid, END)

    if grid == END:
        paths_num += 1
        return

    if grid[1] > 0:
        go_right(grid)
    if grid[0] > 0:
        go_down(grid)
    return

def go_down(grid):
    global paths_num

    grid = [grid[0]-1, grid[1]]

    if grid == END:
        paths_num += 1
        return

    if grid[1] > 0:
        go_right(grid)
    if grid[0] > 0:
        go_down(grid)
    return

grid = [SIZE, SIZE]
run_paths(grid)

print(paths_num)
