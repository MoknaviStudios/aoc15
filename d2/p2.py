file = open("input.txt", "r")

total = 0

for line in file:
    line = line.split("x")
    line = [int(i) for i in line]
    total += line[0] * line[1] * line[2]
    print(total)
    line.sort()
    total += line[0] * 2 + line[1] * 2

file.close()
print(total)