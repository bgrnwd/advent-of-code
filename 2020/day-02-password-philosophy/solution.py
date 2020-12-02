import re
with open("input.txt") as f:
    passwords = [line.strip() for line in f]

# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number
# of times a given letter must appear for the password to be
# valid. For example, 1-3 a means that the password must
# contain a at least 1 time and at most 3 times.
valid = []
for password in passwords:
    fields = password.split(" ")
    char = fields[1].strip(":")
    occurence = [int(o) for o in fields[0].split("-")]
    phrase = list(fields[2])
    if phrase.count(char) in range(occurence[0],occurence[1]+1):
        valid.append(phrase)

print(len(valid))

# Each policy actually describes two positions in the password,
# where 1 means the first character, 2 means the second
# character, and so on. (Be careful; Toboggan Corporate 
# Policies have no concept of "index zero"!) Exactly one of
# these positions must contain the given letter. Other
# occurrences of the letter are irrelevant for the purposes of
# policy enforcement.
count = 0
for password in passwords:
    fields = password.split(" ")
    char = fields[1].strip(":")
    position = [int(o) for o in fields[0].split("-")]
    phrase = list(fields[2])

    indices = [i for i, e in enumerate(phrase) if e == char]
    add_one = [x+1 for x in indices]
    for a in add_one:
        if a in position:
            if not set(position).issubset(set(add_one)):
                count += 1

print(count)
