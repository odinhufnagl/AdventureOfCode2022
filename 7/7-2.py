import enum
file = open("7.txt", "r")
lines = file.readlines()
  
class Dir():
    def __init__(self, name, size, parent, children = []):
        self.name: str = name
        self.size: int = size
        self.children: list[Dir] = children
        self.parent: Dir = parent
    def get_child(self, name: str):
        for child in self.children:
            if (child.name == name):
                return child
    def is_file(self):
        if (len(self.children) == 0):
            return True
        return False 
    def __str__(self):
        return self.name
        
def get_root(cur_dir: Dir):
    if (cur_dir.parent == None):
        return cur_dir
    get_root(cur_dir.parent)

class CMD(enum.Enum):
   LS = "ls"
   CD = "cd"


def is_command(line):
    line = str(line)
    if (line[0] == "$"):
        return True
    return False

def type_of_command(cmd):
    cmd = cmd.split()
    if (cmd[1] == "ls"):
        return CMD.LS
    if (cmd[1] == "cd"):
        return CMD.CD

def cd_location(line):
    line = line.split()
    return line[2]

def navigate_to(place, cur_dir: Dir):
    if (place == ".."):
        return cur_dir.parent
    if (place == "/"):
        return get_root(cur_dir)
    else:
        return cur_dir.get_child(place)

def add_dirs(lines, cur_dir: Dir) -> list[Dir]:
    dirs: list[Dir] = []
    for line in lines:
        line = line.split()
        if (line[0] == "dir"):
            new_dir = Dir(name=line[1], size=0, children=[], parent=cur_dir)
            cur_dir.children.append(new_dir)
            dirs.append(new_dir)
        else:
            new_dir = Dir(name=line[1], size=int(line[0]), children=[], parent=cur_dir)
            cur_dir.children.append(new_dir)
            dirs.append(new_dir)
    return dirs
        


root_dir = Dir(name="root", size=0, parent=None, children=[])
cur_dir: Dir = root_dir
isLS = False
lsCommands = []
for line in lines:
    if (isLS and is_command(line)):
        isLS = False
        dirs = add_dirs(lsCommands, cur_dir)
        lsCommands = []
    elif (isLS):
        lsCommands.append(line)
        continue

    if (is_command(line)):
        command_type = type_of_command(line)
        if (command_type == CMD.CD):
            place_to_navigate = cd_location(line)
            new_dir = navigate_to(place_to_navigate, cur_dir)
            cur_dir = new_dir
        if (command_type == CMD.LS):
            isLS = True
dirs = add_dirs(lsCommands, cur_dir)
def update_sizes(cur_dir: Dir):
    if len(cur_dir.children) == 0:
        return cur_dir.size
    for child in cur_dir.children:
        cur_dir.size += update_sizes(child)
    return cur_dir.size

update_sizes(root_dir)

all_dirs: list[Dir] = []

def store_dir(cur_dir: Dir):
    all_dirs.append(cur_dir)
    for child in cur_dir.children:
        store_dir(child)
store_dir(root_dir)



update_size = 30000000
disk_space = 70000000
root_space = root_dir.size
unused_space = disk_space - root_space

if (unused_space >= update_size):
    print("No need to delete any files")

possible_dirs: list[Dir] = []
for dir in all_dirs:
    if dir.is_file():
        continue
    if (unused_space + dir.size >= update_size):
        possible_dirs.append(dir)

possible_dirs.sort(key=lambda x: x.size)

print(possible_dirs[0].size)





