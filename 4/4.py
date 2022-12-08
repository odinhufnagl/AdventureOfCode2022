f = open("4.txt", "r")
lines = f.readlines()

def sequence(r):
    res = []
    for x in range(r[0], r[1]+1):
        res.append(x)
    return res

def compare_seqs(seq1, seq2):
    hash = {}
    cnt = 0
    for x in seq1:
        hash[x] = True
    for x in seq2:
        if x in hash:
            cnt += 1
    if cnt == len(seq1):
        return True
    return False

count = 0
for line in lines:
    e1, e2 = line.split(",")
    range1, range2 = e1.split("-"), e2.split("-")
    for i in range(2):
        range1[i], range2[i] = int(range1[i].strip()), int(range2[i].strip())
    seq1, seq2 = sequence(range1), sequence(range2)
    if compare_seqs(seq1, seq2) or compare_seqs(seq2, seq1):
        count += 1
print(count)