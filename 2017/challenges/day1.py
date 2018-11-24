"""
Advent of Code 2017 - Day 1
"""
# Day 1
def part1():
    """
    Part 1 Solution
    """
    # Variable declarations
    array = []
    total = 0

    # Open input file
    with open("../inputs/input1.txt", "r") as file:
        for line in file:
            for char in line:
                # for char in file, append to array as an int
                array.append(int(char))

    # Add 1st element to end of array for circularity
    array.append(array[0])

    # Loop through array and check next index for match
    for num in range(0, len(array) - 1):
        if array[num] == array[num+1]:
            # Add to total
            total += array[num]
    # Print answer
    print(total)

def part2():
    """
    Part 2 Solution
    """
    # Variable declarations
    array = []
    total = 0

    # Open input file
    with open("../inputs/input1.txt", "r") as file:
        for line in file:
            for char in line:
                # for char in file, append to array as an int
                array.append(int(char))

    half_length = int(len(array)/2)

    for i in range(0, half_length - 1):
        array.append(array[i])

    # Loop through array and check index for match
    for num in range(0, len(array) - 1):
        try:
            if array[num] == array[num + half_length]:
                # Add to total
                total += array[num]
        except IndexError:
            pass
    # Print answer
    print(total)

def main():
    """
    Main
    """
    part1()
    part2()

if __name__ == "__main__":
    main()
