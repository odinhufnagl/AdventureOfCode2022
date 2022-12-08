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

def score_of_direction(lst, v):
    score = 0
    for x in lst:
        if x >= v:
            score += 1
            break
        score += 1
    return score

def tree_score(grid, i, j, w, h) -> int:
    v = grid[i][j]
    if (is_edge(h, w, i, j)):
        return True
    row = grid[i]
    col = column(grid, j)
    left = row[0:j]
    right = row[j+1:w]
    up = col[0:i]
    up.reverse()
    left.reverse()
    down = col[i+1:h]
    scenic_score = 1
    all_directions = [left, right, up, down]
    for direction in all_directions:
    
        scenic_score *= score_of_direction(direction, v)
    return scenic_score


    
    

grid = read_grid(lines)
h = len(grid)
w = len(grid[0])


best_tree_score = 0

for i in range(h):
    for j in range(w):
            best_tree_score = max(best_tree_score, tree_score(grid, i, j, w, h))

print(best_tree_score)