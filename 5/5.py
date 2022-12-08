f = open("5.txt", "r")
lines = f.readlines()

stacks = [[], [], [], [], [], [], [], [], [], []]
commands = False
def handle_command(command):
    command = command.split()
    amount = int(command[1])
    fromm = int(command[3])-1
    too = int(command[5])-1
    for x in range(amount):
        stacks[too].append(stacks[fromm].pop())

for line in lines:
    line = str(line)
    if commands:
        handle_command(line)
        continue
    if (len(line) == 1):
        commands = True
        continue
    for i in range(0, 9):
        x = 1 + i*4
        if (line[x] != " " and line[i] != str(i+1)):
            stacks[i].insert(0, line[x])
    


ans = ""
for stack in stacks:
    if len(stack) > 0:
        ans += stack[-1]
print(ans)


    
    

