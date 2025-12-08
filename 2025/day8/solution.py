from collections import defaultdict

file = 'input.txt'
numConnections = 10 if file == 'example.txt' else 1000

with open(file, 'r') as f:
    coords = [[int(x) for x in line.strip().split(',')] for line in f]

# store all distances as a list to avoid overwriting duplicates
distances = []
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x, y, z = coords[i]
        a, b, c = coords[j]
        distance = ((x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2) ** 0.5
        distances.append((distance, i, j))

# sort by distances
distances.sort()

# build two-way adjacency list for the connections
connections = defaultdict(list)
for i in range(numConnections):
    _, x, y = distances[i]
    connections[x].append(y)
    connections[y].append(x)

# create all circuits using recursive DFS
visited = set()
circuits = []


def dfs(node, circuit):
    visited.add(node)
    circuit.append(node)
    for neighbour in connections[node]:
        if neighbour not in visited:
            dfs(neighbour, circuit)


for i in range(len(coords)):
    if i not in visited:
        circuit = []
        dfs(i, circuit)
        circuits.append(circuit)

# get the sizes of the three largest circuits
sizes = [len(circuit) for circuit in circuits]
sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
