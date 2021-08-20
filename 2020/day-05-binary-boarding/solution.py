#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

with open("input.txt") as f:
    content = [line.strip() for line in f]

seats_ids = []
seats = defaultdict(list)

def binary_partition(moves: list, space: list, num: int):
    half = len(space)//2
    print(f"Moves: {moves}")
    if len(space) == 1:
        return space[0]

    if moves[num] == 'F' or moves[num] =='L':
        moves.pop(num)
        return binary_partition(moves, space[:half], num)
    elif moves[num] == 'B' or moves[num] == 'R':
        moves.pop(num)
        return binary_partition(moves, space[half:], num)

def calc_seat_id(row: int, col: int):
    print(f"Seat - row {row}, col {col}")
    return 8 * int(row) + int(col)

for c in content:
    chars = [char for char in c]
    print(f"Chars list: {chars}")
    row_chars = chars[:7]
    print(f"Row chars: {row_chars}")
    row_nums = []
    for i in range(0,128):
        row_nums.append(i)
    row = binary_partition(row_chars, row_nums,0) 
    col_chars = chars[-3:]
    print(f"Col chars: {col_chars}")
    col_nums = []
    for i in range(0,8):
        col_nums.append(i)
    col = binary_partition(col_chars, col_nums,0)
    seats_ids.append(calc_seat_id(row,col))
    seats[row].append(col)

print(max(seats_ids))

def find_missing_seat(seats):
    for k in seats.keys():
        for i in range (0,8):
            if i not in seats[k]:
                print(k,i, calc_seat_id(k,i))
find_missing_seat(seats)
