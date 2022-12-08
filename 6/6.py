buff = open("6.txt", "r")
buff = buff.read()

def isMarker(string):
    hash = {}
    for x in string:
        if x in hash:
            return False
        hash[x] = True
    return True


for i in range(len(buff)-3):
    if isMarker(buff[i:i+4]):
        print(i+4)
        break




