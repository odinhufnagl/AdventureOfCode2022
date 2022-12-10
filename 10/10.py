
import enum
file = open("10.txt", "r")
lines = file.readlines()

class CommandType(enum.Enum):
    ADD_X = "addX"
    NOOP = "noop"
    def __str__(self) -> str:
        return super().__str__()

class Command():
    def __init__(self, command_type, val):
        self.command_type = str_to_command(command_type)
        self.value = val
        self.cycles = command_type_to_cycles(self.command_type)


def command_type_to_cycles(command_type):
    switcher = {
        CommandType.ADD_X: 2,
        CommandType.NOOP: 1,
    }
    return switcher[command_type]
    

def str_to_command(str):
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
for line in lines:

    if (len(line.split()) == 1):
        command_type, val = line.strip(), None
    else:
        command_type, val = line.split()
    command = Command(command_type, val)
    for cycle in range(command.cycles):
        if (cycle_count in signal_strength_indexes):
            sum += cycle_count * x
        cycle_count += 1
        if (cycle == 1 and command.command_type == CommandType.ADD_X):
            x += int(command.value)


print(sum)