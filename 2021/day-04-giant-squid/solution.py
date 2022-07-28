import collections
import re

with open("data.in") as f:
    data = [line.strip() for line in f]

numbers_to_call = [int(n) for n in data[0].split(",")]
boards_lines = data[2:]

boards = []
board = []
for line in boards_lines:
    if line == '':
        boards.append(board)
        board.clear()
    else:
        board.append([int(val) for val in line.strip().split()])

for n in numbers_to_call:
    for b in boards:
        for row in b:
            if n in row:
                pass