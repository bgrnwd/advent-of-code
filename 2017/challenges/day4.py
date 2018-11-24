"""
Advent of Code 2017 - Day 4
"""

def part1():
    """
    Part 1 Solution
    """
    # Variable declaration
    valid = 0

    # Open input file
    with open("../inputs/input4.txt", "r") as file:
        for line in file:
            # Remove new line character
            no_line = line.rstrip()
            # Split line by spaces
            passphrases = no_line.split(" ")
            # Remove duplicates if there are any
            check = set(passphrases)
            # If len of set and orignal list is the same, increment counter
            if len(check) == len(passphrases):
                valid += 1
    print(valid)

def part2():
    """
    Part 2 Solution
    """
    def has_anagram(passphrase):
        """
        Checks if a list has items that are anagrams
        """
        for i in range(len(passphrase)):
            for j in range(i + 1, len(passphrase)):
                phrase1 = sorted(passphrase[i])
                phrase2 = sorted(passphrase[j])
                if phrase1 == phrase2:
                    return True
    # Variable declaration
    valid = 0

    # Open input file
    with open("../inputs/input4.txt", "r") as file:
        for line in file:
            # Remove new line character
            no_line = line.rstrip()
            # Split line by spaces
            passphrases = no_line.split(" ")
            # Remove duplicates if there are any
            check = set(passphrases)
            # If len of set and orignal list is the same, increment counter
            if len(check) == len(passphrases):
                if has_anagram(passphrases) != True:
                    valid += 1
    print(valid)

def main():
    """
    Main
    """
    part1()
    part2()

if __name__ == "__main__":
    main()
