import re
pattern = re.compile("\S{3}:\S*")
passports = []
with open("input.txt") as f:
    content =  [line.strip() for line in f]
port = {}
for c in content:
    reg = pattern.findall(c)
    if reg:
        for r in reg:
            k,v = r.split(":")
            port[k] = v
    else:
        passports.append(port)
        port = {}

valid_keys = set(["byr","iyr","eyr","hgt","hcl","ecl","pid"])
#valid = 0
#for passport in passports:
#    if "cid" in passport:
#        passport.pop("cid")
#    if valid_keys - set(passport.keys()) == set():
#        valid += 1
#print(valid)

valid = 0
eyes = ["amb","blu","brn","gry","grn","hzl","oth"]
for passport in passports:
    if "cid" in passport:
        passport.pop("cid")
    if valid_keys - set(passport.keys()) == set() \
    and re.match("\d{4}",passport["byr"]) and int(passport["byr"]) >= 1920 and int(passport["byr"]) <=2002 \
    and re.match("\d{4}",passport["iyr"]) and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <=2020 \
    and re.match("\d{4}",passport["eyr"]) and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <=2030 \
    and re.match("^\d{9}$", passport["pid"]) \
    and passport["ecl"] in eyes \
    and re.match("#[\da-f]{6}",passport["hcl"]) \
    and (passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193 or passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76):
        valid += 1
print(valid)
