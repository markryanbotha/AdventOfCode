from collections import Counter
file = 'example.txt'
numConnections = 10 if file == 'example.txt' else 1000

with open(file, 'r') as f:
    coords = [[int(x) for x in line.strip().split(',')] for line in f]

# Store all distances as a list with (distance, node1, node2)
# Use a list as it avoids overwriting if distances happen to be the same
distances = []
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x, y, z = coords[i]
        a, b, c = coords[j]
        distance = ((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2) ** 0.5
        distances.append((distance, i, j))

# sort the array by distances
distances.sort()

# each node starts in it's own circuit
# node 0 points to itself, node 1 points to itself and so on
parent = list(range(len(coords)))


# find which circuit a node is in
# recursively jump around circuit until a node is it's own parent
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


# merges circuits which means make left node point to right node
# this is indicated by node[x] = y, where node at index x has value of y
# so when you jump to y, you can then jump to node until it is node[x] = x
def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        parent[px] = py


# merge the closest pairs up to numConnections
# where x, y are nodes that should be connected
for i in range(numConnections):
    _, x, y = distances[i]
    union(x, y)

print(parent)

# count sizes of each circuit
sizes = list(Counter(find(i) for i in range(len(coords))).values())
print(sizes)
sizes.sort(reverse=True)
solution = 1
for i in range(3):
    solution *= sizes[i]
print(solution)
