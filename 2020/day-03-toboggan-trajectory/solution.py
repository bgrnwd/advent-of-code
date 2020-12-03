with open("input.txt") as f:
    inp = [line.strip()*100 for line in f]
slope = 3
tree = 0
for idx,item in enumerate(inp):
    if idx == 0:
        continue
    char_list = [char for char in item]
    try:
        if char_list[slope] ==  '#':
            tree += 1
        slope += 3
    except:
        print(f"Index error: {slope}")
        break

print(tree)

slopes = [(3,1), (1,1),(5,1),(7,1),(1,2)]
trees = []
for s in slopes:
    right = s[0]
    down = s[1]
    count = 0
    index = right
    for idx,item in enumerate(inp):
        if idx not in range(down,len(inp),down):
            continue
        char_list = [char for char in item]
        try:
            if char_list[index] ==  '#':
                count += 1
            index += right
        except:
            print(f"Index error: {index}")
            break
    trees.append(count)
result = 1
print(trees)
for t in trees:
    result *= t
print(result)
    


