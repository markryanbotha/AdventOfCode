from collections import defaultdict

graph = defaultdict(list)

with open("input.txt", "r") as f:
    for line in f:
        input, output = line.strip().split(":")
        for device in output.split(" "):
            if len(device) > 0:
                graph[input].append(device)


stack = []
for device in graph.keys():
    if device == 'you':
        stack.extend(graph[device])
solution = 0
while stack:
    device = stack.pop()
    if device == 'out':
        solution += 1
    else:
        stack.extend(graph[device])

print(solution)
