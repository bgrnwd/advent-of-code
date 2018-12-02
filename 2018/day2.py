# https://adventofcode.com/2018/day/2
import itertools
import collections

def part1():
    box_ids = []
    twos = 0
    threes = 0

    with open("./inputs/day2.txt", "r") as file:
        for line in file:
            box_ids.append(line)

    for i in box_ids:
        d = collections.defaultdict(int)

        # Counts number of times a char repeats in a given box id and adds to a dict
        for char in i:
            d[char] += 1

        # If a char repeats twice in a box id, add to twos and only count the id once
        for value in d.values():
            if value == 2:
                twos += 1
                break

        # If a char repeats thrice in a box id, add to threes and only count the id once
        for value in d.values():
            if value == 3:
                threes += 1
                break
                
    # Calculate the checksum by multiplying the num of box ids with 2 repeating chars and 3 repeating chars
    print(twos * threes)

def part2():
    box_ids = []

    with open("./inputs/day2.txt", "r") as file:
        for line in file:
            box_ids.append(line)

    #Compare each box id to all others
    for a,b in itertools.combinations(box_ids, 2):
        # Create tuple of 2 ids
        ids = zip(a,b)

        # Checks char at each position and if they are not the same returns num of differences
        differ = len([c for c,d in ids if c!=d])

        # If the difference is only once, displays the chars both ids have in common
        if differ == 1:
            l1 = list(a)
            l2 = list(b)
            common_chars = []
            for idx, val in enumerate(l1):
                if l1[idx] == l2[idx]:
                    common_chars.append(l1[idx])
            print(''.join(common_chars))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
