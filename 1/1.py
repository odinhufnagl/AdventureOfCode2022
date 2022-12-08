f = open("1.txt", "r")

elves = [0]
lines = f.readlines()
for line in lines:
    if line == "\n":
        elves.append(0)
        continue
    elves[-1] += int(line)
print(sum(sorted(elves)[-3:]))


