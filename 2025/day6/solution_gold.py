from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [] 
    for line in f: 
        lines.append([value for value in line if len(value) > 0 and value != '\n'])

# Group by column
def groupByColumn(rows):
    g = defaultdict(list) 
    for i, line in enumerate(rows): 
        for j, value in enumerate(line):
            g[j].append(value)
    return list(g.values())

# Remove any empty spaces that remain / needs to happen after to allow for columns to stay intact
def removeEmpty(groups):
    processed = []
    for group in groups:
        current = []
        for char in group:
            if char != " ":
                current.append(char)
        if len(current) > 0:
            processed.append(current)
    return processed

grouped = removeEmpty(groupByColumn(lines))

combined = []
curr = []
# Iterate through column groups, if column group has operation, create new list of operation + column group nums i.e. ['*', 1, 24, 356]
for c in grouped:
    if c[-1] == "+" or c[-1] == "*":
        # Avoid empty list in beginning
        if len(curr) != 0: 
            # If we see an operation, we know we are starting a new list 
            # finalise the old one
            combined.append(curr)
        # reset list after finalising
        curr = []
        operation = c.pop()
        # add operation to current list 
        curr.append(operation)
        # turn list of nums into a single value, add to 
        curr.append(int(''.join(c)))
    else:
        curr.append(int(''.join(c)))
# Final operation with ongoing operation (as we only finalise when we see an operation, so last one needs to be done manually as no operation comes after)
combined.append(curr)

# Need different defaultValue for * or +
defaultValue = {'*': 1, "+": 0 }
solution = 0
for c in combined:
    # get operation from beginning of list
    operation = c.pop(0)
    value = defaultValue[operation]
    # iterate over remaining values of list
    for n in c:
        if operation == "*":
            value *= n
        else:
            value += n
    solution += value

print(solution)


