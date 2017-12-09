"""
Advent of Code 2017 - Day 5
"""

def part1():
    """
    Part 1 Solution
    """
    # Variable declaration
    jumps = []
    steps = 0
    index = 0

    # Open input file
    with open("../inputs/input5.txt", "r") as file:
        for line in file:
            # Remove new line character
            no_line = line.rstrip()
            # Add line to list
            jumps.append(int(no_line))

    # Jumps
    while index >= 0 and index < len(jumps):
        steps += 1
        prev_index = index
        next_index = index + jumps[index]
        jumps[prev_index] += 1
        index = next_index
    print(steps)

def part2():
    """
    Part 2 Solution
    """
    # Variable declaration
    jumps = []
    steps = 0
    index = 0

    # Open input file
    with open("../inputs/input5.txt", "r") as file:
        for line in file:
            # Remove new line character
            no_line = line.rstrip()
            # Add line to list
            jumps.append(int(no_line))

    # Jumps
    while index >= 0 and index < len(jumps):
        steps += 1
        prev_index = index
        next_index = index + jumps[index]
        if jumps[prev_index] >= 3:
            jumps[prev_index] -= 1
        else:
            jumps[prev_index] += 1

        index = next_index
    print(steps)

def main():
    """
    Main
    """
    part1()
    part2()

if __name__ == "__main__":
    main()
