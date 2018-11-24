"""
Advent of Code 2017 - Day 3
"""
# Imports
from itertools import cycle

def part1(max_num):
    """
    Day 3 Solution
    """
    # Movements to traverse grid
    def move_right(x_coord, y_coord):
        """
        Move right, increase x position by 1
        """
        return x_coord+1, y_coord

    def move_down(x_coord, y_coord):
        """
        Move down, decrease y position by 1
        """
        return x_coord, y_coord-1

    def move_left(x_coord, y_coord):
        """
        Move left, decrease x position by 1
        """
        return x_coord-1, y_coord

    def move_up(x_coord, y_coord):
        """
        Move up, increase y position by 1
        """
        return x_coord, y_coord+1

    moves = [move_right, move_down, move_left, move_up]
    def generate(max_num):
        """
        Generates values and coordinates for spiral grid
        """
        _moves = cycle(moves)
        num = 1
        pos = 0, 0
        times_to_move = 1

        yield num, pos

        while True:
            for _ in range(2):
                move = next(_moves)
                for _ in range(times_to_move):
                    if num >= max_num:
                        return
                    pos = move(*pos)
                    num += 1
                    yield num, pos
            times_to_move += 1

    grid = list(generate(max_num))
    dist = abs(grid[-1][1][0] - grid[0][1][0]) + abs(grid[-1][1][1] - grid[0][1][1])
    print(dist)

def main():
    """
    Main
    """
    part1(289326)

if __name__ == "__main__":
    main()
