f = open("2.txt", "r")
lines = f.readlines()


d = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY":5 , "BZ": 9, "CX": 7, "CY":2, "CZ":6}

sum = 0
for line in lines:
    elf, you = line[0], line[2]
    sum += d[elf+you]

print(sum)