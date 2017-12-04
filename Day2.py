"""
Advent of Code 2017 - Day 2
"""
# Import regex
import re

def day2():
    """
    Day 2 Solution
    """
    # Variable declarations
    checksum = 0

    # Open input file
    with open("./inputs/input2.txt", "r") as file:
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

def main():
    """
    Main
    """
    day2()

if __name__ == "__main__":
    main()
