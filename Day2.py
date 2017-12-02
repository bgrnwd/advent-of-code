# Import regex
import re 
# Day 2
def Day2():
    # Variable declarations
    checksum = 0

    # Open input file
    with open("./inputs/input2.txt", "r") as file:
        for line in file:
            # Remove new line character
            noLine = line.rstrip()
            # Split numbers by tabs
            numbers = re.split(r'\t+', noLine)
            # Convert string array to int array
            ints = map(int, numbers)
            # Calculations
            minimum = min(ints)
            maximum = max(ints)
            diff = maximum -  minimum
            checksum += diff
        print checksum


def main():
    Day2()

if __name__ == "__main__":
    main()          