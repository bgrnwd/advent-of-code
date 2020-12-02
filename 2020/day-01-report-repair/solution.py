import itertools

with open("report-repair.txt") as f:
    report = f.read().splitlines()

report = [int(i) for i in report]

# Find the two entries that sum to 2020; 
# what do you get if you multiply them together?
for n in report:
    diff = 2020 - n
    if diff in report:
        print(diff * n)
        break

# what is the product of the three entries that sum to 2020?
for a, b, c in itertools.combinations(report, 3):
    if a + b + c == 2020:
        print(a*b*c)
        break
