file = open("input.txt", "r")

total = 0
sides = []

for line in file:
    line = line.split("x")
    sides.append(int(line[0]) * int(line[1]))
    sides.append(int(line[1]) * int(line[2]))
    sides.append(int(line[0]) * int(line[2]))
    total += (2 * sum(sides))
    total += min(sides)
    sides = []


file.close()
print(total)