with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

rows = len(lines)
cols = len(lines[0])

start = lines[0].index('S')

paths = [[0] * cols for _ in range(rows)]
paths[0][start] = 1

for r in range(rows - 1):
    for c in range(cols):
        # not a beam, ignore
        if paths[r][c] == 0:
            continue

        if lines[r + 1][c] == '^':
            if c > 0:
                # create new beam to right
                # We do += paths[r][c] to increase value by number of beams that are already in current path 
                paths[r + 1][c - 1] += paths[r][c]
            if c < cols - 1:
                # do the same to the left of splitter
                paths[r + 1][c + 1] += paths[r][c]
        else:
            # otherwise, continue path right above
            paths[r + 1][c] += paths[r][c]

print(sum(paths[-1]))
