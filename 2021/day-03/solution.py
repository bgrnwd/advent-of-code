import collections
import re

with open("data.in") as f:
    data = [line.strip() for line in f]

def gamma_rate(numbers: list) -> str:
    rate = ""
    common = {}
    for i in range(len(numbers[0])):
        common[str(i)] = ""
    for num in numbers:
        for i in range(len(num)):
            common[str(i)] = common[str(i)] + str(num[i])
    for k,v in common.items():
        if v.count("1") >= v.count("0"):
            rate += "1"
        else:
            rate += "0"
    return rate

def flip_bits(bits: str) -> str:
    return "".join('1' if b == '0' else '0' for b in bits)

gr = gamma_rate(data)
er = flip_bits(gr)
print(gr, er)

gr_dec = int(gr, 2)
er_dec = int(er, 2)
print(er_dec * gr_dec)

def rating(numbers: list, rating_type: str):
    bnumbers = numbers.copy()
    for i in range(len(numbers[0])):
        if rating_type == "oxygen":
            common_bits = list(gamma_rate(bnumbers))
        else:
            common_bits = list(flip_bits(gamma_rate(bnumbers)))
        for b in bnumbers:
            if int(b[i]) == int(common_bits[i]):
                pass
            else:
                bnumbers = list(filter((b).__ne__, bnumbers))
        if len(bnumbers) == 1:
            return bnumbers[0]

oxr = rating(data, "oxygen")
cor = rating(data, "co2")

print(oxr, cor)
print(int(oxr, 2) * int(cor, 2))