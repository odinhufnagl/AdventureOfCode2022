import enum

file = open("9.txt", "r")
lines = file.readlines()

class Direction(enum.Enum):
    R = "right"
    L = "left"
    U = "up"
    D = "down"

class Position():
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def add(self, pos):
        self.i += pos.i
        self.j += pos.j

    def has_neighbour(self, pos):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if self.i + di == pos.i and self.j + dj == pos.j:
                    return True
        return False
        
    def copy(self):
        return Position(self.i, self.j)
    def __str__(self) -> str:
        return str(self.i) + " " + str(self.j)

def str_to_direction(str):
    switcher = {
        "R": Direction.R,
        "L": Direction.L,
        "U": Direction.U,
        "D": Direction.D
    }
    return switcher[str]

def direction_to_delta_position(dir) -> Position:
    switcher = {
        Direction.R: Position(0, 1),
        Direction.L: Position(0, -1),
        Direction.U: Position(-1,0),
        Direction.D: Position(1, 0)
    }
    return switcher[dir]


def pos_already_exist(lst, pos):
    for p in lst:
        if p.i == pos.i and p.j == pos.j:
            return True
    return False

def grid_measures(lst: list[Position]):
    min_i = 0
    max_i = 0
    min_j = 0
    max_j = 0
    for pos in lst:
        min_i = min(pos.i, min_i)
        min_j = min(pos.j, min_j)
        max_i = max(pos.i, max_i)
        max_j = max(pos.j, max_j)  
    w = 1 + max_j - min_j
    h = 1 + max_i - min_i
    return (w, h, -min_i, -min_j)

h_pos = Position(0, 0)
t_pos = Position(0, 0)
h_positions: list[Position] = [h_pos.copy()]
t_positions: list[Position] = [t_pos.copy()]
for line in lines:
    dir, step_count = line.split(" ")
    step_count = int(step_count)
    dir = str_to_direction(dir)
    delta_position = direction_to_delta_position(dir)
    h_pos_prev = h_pos
    for step in range(step_count):
        h_pos_prev = h_pos.copy()
        h_pos.add(delta_position)
        h_positions.append(h_pos.copy())
        if (not t_pos.has_neighbour(h_pos)):
            t_pos = h_pos_prev.copy()
            if (not pos_already_exist(t_positions, t_pos)):
                t_positions.append(t_pos.copy())
    
        

w, h, delta_i, delta_j = grid_measures(h_positions)


for pos in t_positions:
    delta_position = Position(delta_i, delta_j)
    pos.add(delta_position)

resultGrid = [["." for x in range(w)] for y in range(h)]
for index in range(len(t_positions)):
    pos = t_positions[index]
    if (index == 0):
        resultGrid[pos.i][pos.j] = "s"
    else:
        resultGrid[pos.i][pos.j] = "#"

#for row in resultGrid:
   # print("".join(row))
print(len(t_positions))