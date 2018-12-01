"""
Advent of Code 2018 - Day 1
"""
from itertools import cycle
# Day 1
def part1():
    """
    Part 1 Solution
    """
    frequency_changes = []
    starting_frequency = 0

    # Open input file
    with open("./part1_input.txt", "r") as file:
        for line in file:
            frequency_changes.append(line)
    # Calculate frequency
    for f in frequency_changes:
        starting_frequency += int(f)

    print(starting_frequency)

def part2():
    """
    Part 2 Solution
    """
    frequency_changes = []
    intermediate_frequencies = set()
    frequency = 0

    # Open input file
    with open("./part2_input.txt", "r") as file:
        for line in file:
            frequency_changes.append(line)

    repeat_frequency = cycle(frequency_changes)

    for f in repeat_frequency:
        frequency += int(f)
        if frequency in intermediate_frequencies:
            print(frequency)
            return
        else:
            intermediate_frequencies.add(frequency)

def main():
    """
    Main
    """
    part1()
    part2()

if __name__ == "__main__":
    main()
