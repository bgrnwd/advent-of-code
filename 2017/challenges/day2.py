"""
Advent of Code 2017 - Day 2
"""
# Import regex
import re

def part1():
    """
    Part 1 Solution
    """
    # Variable declarations
    checksum = 0

    # Open input file
    with open("../inputs/input2.txt", "r") as file:
        for line in file:
            # Remove new line character
            no_line = line.rstrip()
            # Split numbers by tabs
            numbers = re.split(r'\t+', no_line)
            # Convert string array to int array
            ints = list(map(int, numbers))
            # Calculations
            minimum = min(ints)
            maximum = max(ints)
            diff = maximum -  minimum
            checksum += diff
        print(checksum)

def part2():
    """
    Part 2 Solution
    """
    # Variable declarations
    checksum = 0

    # Open input file
    with open("../inputs/input2.txt", "r") as file:
        for line in file:
            # Remove new line character
            no_line = line.rstrip()
            # Split numbers by tabs
            numbers = re.split(r'\t+', no_line)
            # Convert string array to int array
            ints = list(map(int, numbers))
            # Calculations
            for i in range(len(ints)):
                try:
                    divisor = ints.pop(i)
                    for j in range(len(ints)):
                        if ints[j] % divisor == 0:
                            checksum += ints[j]/divisor
                    ints.insert(i, divisor)
                except IndexError:
                    pass
        print(checksum)

def main():
    """
    Main
    """
    part1()
    part2()

if __name__ == "__main__":
    main()
