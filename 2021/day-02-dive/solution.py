import collections
import re

with open("data.in") as f:
    data = [line.strip() for line in f]

movements = []

for d in data:
    mv = d.split(" ")
    movements.append([mv[0], int(mv[1])])

# horizontal, depth
sub_pos = [0,0]

for m in movements:
    if m[0] == "forward":
        sub_pos[0] += m[1]
    elif m[0] == "down":
        sub_pos[1] += m[1]
    elif m[0] == "up":
        sub_pos[1] -= m[1]

print(sub_pos)
print(sub_pos[0] * sub_pos[1])

# horizontal, depth, aim
sub_pos_two = [0,0,0]

for m in movements:
    if m[0] == "forward":
        sub_pos_two[0] += m[1]
        sub_pos_two[1] += sub_pos_two[2] * m[1]
    elif m[0] == "down":
        sub_pos_two[2] += m[1]
    elif m[0] == "up":
        sub_pos_two[2] -= m[1]

print(sub_pos_two)
print(sub_pos_two[0] * sub_pos_two[1])

