with open('input.txt', 'r') as f:
    coords = [[int(x) for x in line.strip().split(',')] for line in f]

distances = []
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x, y, z = coords[i]
        a, b, c = coords[j]
        distance = ((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2) ** 0.5
        distances.append((distance, i, j))

distances.sort()

parent = list(range(len(coords)))


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# Count successful merges until we have 1 circuit
# Each merge reduces the number of circuits by 1
merges = 0
for dist, i, j in distances:
    pi, pj = find(i), find(j)
    # not already in same circuit, so merge
    if pi != pj:
        parent[pi] = pj
        merges += 1
        # N - 1 merges means this is the last merge
        # that would be made
        if merges == len(coords) - 1:
            print(coords[i][0] * coords[j][0])
            break
