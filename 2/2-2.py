f = open("2.txt", "r")
lines = f.readlines()


d = {"AX": 3+0, "AY": 1+3, "AZ": 2+6, "BX": 1+0, "BY":2+3 , "BZ": 3+6, "CX": 2+0, "CY":3+3, "CZ":1+6}

sum = 0
for line in lines:
    elf, you = line[0], line[2]
    sum += d[elf+you]

print(sum)