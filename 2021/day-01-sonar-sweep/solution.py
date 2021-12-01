
with open("data.in") as f:
    data = [int(line) for line in f]

measurements = 0
for idx, val in enumerate(data):
    if idx != 0:
        if data[idx] > data[idx-1]:
            measurements += 1

measure = 0
for i in range(3, len(data)):
    a = data[i-1] + data[i-2] + data[i-3]
    b = data[i] + data[i-1] + data[i-2]
    if b > a:
        measure +=1

print(measurements)
print(measure)