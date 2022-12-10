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


def get_new_pos(current_pos, previous_pos) -> Position:
    # under
    if (previous_pos.i > current_pos.i and previous_pos.j == current_pos.j):
        return Position(current_pos.i+1, current_pos.j)
    # over
    if (previous_pos.i < current_pos.i and previous_pos.j == current_pos.j):
        return Position(current_pos.i-1, current_pos.j)
    # right
    if (previous_pos.j > current_pos.j and previous_pos.i == current_pos.i):
        return Position(current_pos.i, current_pos.j+1)
    # left
    if (previous_pos.j < current_pos.j and previous_pos.i == current_pos.i):
        return Position(current_pos.i, current_pos.j-1)
    # diagonal

    #top right
    if (previous_pos.j > current_pos.j and previous_pos.i < current_pos.i):
        return Position(current_pos.i-1, current_pos.j+1)
    #top left
    if (previous_pos.j < current_pos.j and previous_pos.i < current_pos.i):
        return Position(current_pos.i-1, current_pos.j-1)
    #bottom left
    if (previous_pos.j < current_pos.j and previous_pos.i > current_pos.i):
        return Position(current_pos.i+1, current_pos.j-1)
    #bottom right
    if (previous_pos.j > current_pos.j and previous_pos.i > current_pos.i):
        return Position(current_pos.i+1, current_pos.j+1)



tail_positions = [Position(0, 0)]
current_positions = [Position(0, 0) for y in range(10)]



cnt = 0

for line in lines:
    dir, step_count = line.split(" ")
    step_count = int(step_count)
    dir = str_to_direction(dir)
    delta_position = direction_to_delta_position(dir)
    for step in range(step_count):
        for knot_index, knot_pos in enumerate(current_positions):
            if knot_index == 0:
                 new_pos = knot_pos.copy()
                 new_pos.add(delta_position)
                 current_positions[knot_index] = new_pos
                 continue
            if (not knot_pos.has_neighbour(current_positions[knot_index-1])):
                new_pos = get_new_pos(knot_pos, current_positions[knot_index-1])
                current_positions[knot_index] = new_pos
                if (knot_index == 9 and not pos_already_exist(tail_positions, new_pos)):
                    tail_positions.append(new_pos.copy())

        

#print(all_positions[9])
print(len(tail_positions))