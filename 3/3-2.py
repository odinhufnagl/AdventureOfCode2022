f = open("3.txt", "r")
rucksacks = f.readlines()

def find_similar_item(lst, group_len):
    hash = {}
    for rucksack in lst:
        rucksack = set(rucksack)
        for item in rucksack:
            if item not in hash:
                hash[item] = 0
            hash[item] += 1
    for key in hash.keys():
        if hash[key] == group_len:
            return key

sum = 0
alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
group_len = 3
for i in range(0, len(rucksacks), 3):
    rucksacks_in_group = rucksacks[i: i+group_len]
    rucksacks_in_group = map(lambda x: x.strip(), rucksacks_in_group)
    similar_item = find_similar_item(rucksacks_in_group, group_len)
    sum += alphabet.index(similar_item)

print(sum)
