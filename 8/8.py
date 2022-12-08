import re

file = open("8.txt", "r")
lines = file.readlines()

def read_grid(lines) -> list[list[int]]:
    grid = []
    for line in lines:
        row = [*line.strip()]
        grid.append(row)
    return grid

def is_edge(h, w, i, j) -> bool:
    return i == w-1 or i == 0 or j == h-1 or j == 0

def column(matrix, j):
    return [row[j] for row in matrix]

def is_all_number_smaller(lst, v):
    for x in lst:
        if x >= v:
            return False
    return True

def is_tree_visible(grid, i, j, w, h) -> bool:
    v = grid[i][j]
    if (is_edge(h, w, i, j)):
        return True
    row = grid[i]
    col = column(grid, j)
    left = row[0:j]
    right = row[j+1:w]
    up = col[0:i]
    down = col[i+1:h]
    all_directions = [left, right, up, down]
    for direction in all_directions:
        if (is_all_number_smaller(direction, v)):
            return True
    
    return False
    
grid = read_grid(lines)
h = len(grid)
w = len(grid[0])


trees_count = 0

for i in range(h):
    for j in range(w):
        if (is_tree_visible(grid, i, j, w, h)):
            trees_count += 1

print(trees_count)