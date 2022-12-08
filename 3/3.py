f = open("3.txt", "r")
rucksacks = f.readlines()

def find_similar_items(c1, c2):
    similar_items = []
    hash = {}
    for item in c1:
        hash[item] = True
    for item in c2:
        if item in hash:
            similar_items.append(item)
    return set(similar_items)


sum = 0
alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for rucksack in rucksacks:
    rucksack = rucksack.strip()
    comp_size = int(len(rucksack) / 2)
    c1, c2 = rucksack[0: comp_size], rucksack[comp_size: len(rucksack)]
    similar_items = find_similar_items(c1, c2)

    for item in similar_items:
        sum += alphabet.index(item)

print(sum)

