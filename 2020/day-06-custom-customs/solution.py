from collections import defaultdict
groups = []
with open("input.txt") as f:
    group = []
    for line in f:
        line = line.strip()
        if not line:
            groups.append(group)
            group = []
        else:
            group.append(line)
counts = 0
for g in groups:
    s = set()
    for item in g:
        for char in item:
            s.add(char)
    counts += len(s)
print(counts)

alls = 0
for g in groups:
    answers = defaultdict(int)
    for item in g:
        for char in item:
            answers[char] += 1
    for k,v in answers.items():
        if len(g) == v:
            alls += 1
print(alls)
