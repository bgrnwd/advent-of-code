# https://adventofcode.com/2018/day/1
from itertools import cycle

def part1():
    frequency_changes = []
    starting_frequency = 0

    with open("./inputs/day1.txt", "r") as file:
        for line in file:
            frequency_changes.append(line)

    # Add frequencies together to get final frequency
    for f in frequency_changes:
        starting_frequency += int(f)

    print(starting_frequency)

def part2():
    frequency_changes = []
    intermediate_frequencies = set()
    frequency = 0

    with open("./inputs/day1.txt", "r") as file:
        for line in file:
            frequency_changes.append(line)

    # Set up circular list
    repeat_frequency = cycle(frequency_changes)

    # Continously cycle through the list of frequencies
    for f in repeat_frequency:
        frequency += int(f)
        # Find the first frequency sum that repeats
        if frequency in intermediate_frequencies:
            print(frequency)
            return
        else:
            intermediate_frequencies.add(frequency)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
