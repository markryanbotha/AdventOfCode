from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [] 
    for line in f: 
        values = line.strip().split(" ")
        lines.append([value for value in values if len(value) > 0])

# Group by column
g = defaultdict(list) 
for i, line in enumerate(lines): 
    for j, value in enumerate(line):
        g[j].append(value)
grouped = list(g.values())

# Need different defaultValue for * or +
defaultValue = {'*': 1, "+": 0 }
solution = 0
for group in grouped:
    # get sign from back of group
    sign = group.pop()
    value = defaultValue[sign]
    # process rest of group
    for n in group:
        n = int(n)
        if sign == "*":
            value *= n
        elif sign == "+":
            value += n
    solution += value


print(solution)

