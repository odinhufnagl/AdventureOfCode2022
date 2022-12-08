buff = open("6.txt", "r").read()
def isMarker(string):
    hash = {}
    for x in string:
        if x in hash:
            return False
        hash[x] = True
    return True
    
for i in range(len(buff)-13):
    if isMarker(buff[i:i+14]):
        print(i+14)
        break
