# https://adventofcode.com/2018/day/3
import collections

class claim:
    top = 0
    left = 0
    length = 0
    width = 0
    ID = 0

    def __init__(self, id, left, top, width, length):
        self.top = top
        self.left = left
        self.ID = id
        self.length = length
        self.width = width

def part1():
    claims = []
    coords = []
    grid = collections.defaultdict(int)

    # Parse input into claim object
    with open("./inputs/day3.txt", "r") as file:
        for line in file:
            attrs = line.split(' ')
            claimID = int(attrs[0].replace('#',''))
            pos = attrs[2].replace(':','').split(',')
            left = int(pos[0])
            top = int(pos[1])
            area = attrs[3].replace('\n','').split('x')
            width = int(area[0])
            length = int(area[1])
            claims.append(claim(claimID,left,top,width,length))

    # Calculate x,y positions of each square
    for c in claims:
        for w in range(c.width):
            for l in range(c.length):
                coords = (c.left + w, c.top + l)
                # Count each time a coordinate appears
                grid[coords] += 1

    overlaps = 0
    for v in grid.values():
        if v >= 2:
            overlaps += 1

    print(overlaps)

def part2():
    claims = []
    coords = []
    grid = collections.defaultdict(int)

    # Parse input into claim object
    with open("./inputs/day3.txt", "r") as file:
        for line in file:
            attrs = line.split(' ')
            claimID = int(attrs[0].replace('#',''))
            pos = attrs[2].replace(':','').split(',')
            left = int(pos[0])
            top = int(pos[1])
            area = attrs[3].replace('\n','').split('x')
            width = int(area[0])
            length = int(area[1])
            claims.append(claim(claimID,left,top,width,length))

    # Calculate x,y positions of each square
    for c in claims:
        for w in range(c.width):
            for l in range(c.length):
                coords = (c.left + w, c.top + l)
                # Count each time a coordinate appears
                grid[coords] += 1

    for c in claims:
        overlap = False
        for w in range(c.width):
            for l in range(c.length):
                coords = (c.left + w, c.top + l)
                # Count each time a coordinate appears
                if grid[coords] > 1:
                    overlap = True
        if overlap == False:
            print(c.ID)
def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
