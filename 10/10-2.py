
import enum
import math
file = open("10.txt", "r")
lines = file.readlines()

class CommandType(enum.Enum):
    ADD_X = "addX"
    NOOP = "noop"
    def __str__(self) -> str:
        return super().__str__()

class Command():
    def __init__(self, command_type, val):
        self.command_type = self.__str_to_command(command_type)
        self.value = val
        self.cycles = self.__init_cycles()

    def __init_cycles(self):
        switcher = {
            CommandType.ADD_X: 2,
            CommandType.NOOP: 1,
        }
        return switcher[self.command_type] 

    def __str_to_command(self, str):
        switcher = {
            "addx": CommandType.ADD_X,
            "noop": CommandType.NOOP,
        }
        return switcher[str]

cycle_count = 0

sum = 0
signal_strength_indexes = [20, 60, 100, 140, 180, 220]
cycle_count = 1
x = 1

w = 40
h = 6

crt_grid = [["." for x in range(w)] for y in range(h)]

for line in lines:

    if (len(line.split()) == 1):
        command_type, val = line.strip(), None
    else:
        command_type, val = line.split()
    command = Command(command_type, val)
    for cycle in range(command.cycles):
        crt_position = cycle_count-1
        print(crt_position, x)
        cycle_count += 1
        if (crt_position % w >= x-1 and crt_position % w <= x+1):
            crt_grid[math.floor(crt_position / w)][crt_position % w] = "#"
        if (cycle == 1 and command.command_type == CommandType.ADD_X):
            x += int(command.value)


print(sum)

for row in crt_grid:
    print("".join(row))
