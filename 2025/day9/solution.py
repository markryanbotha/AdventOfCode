with open("input.txt", "r") as f:
    c = [line.split(",") for line in f]
    coords = [(int(line[0].strip()), int(line[1].strip())) for line in c]

# Just straight up brute forcing it
maximum = 0
for i in range(len(coords)):
    for j in range(i, len(coords)):
        # inclusive of current line with the + 1
        x = abs(coords[i][0] - coords[j][0]) + 1
        y = abs(coords[i][1] - coords[j][1]) + 1
        area = x * y
        maximum = max(maximum, area)


print(maximum)
