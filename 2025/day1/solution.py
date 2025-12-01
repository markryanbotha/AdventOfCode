lines = []

with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line)


curr = 50
solution = 0
for line in lines:
    amount = int(line[1:])
    if line.startswith("L"):
        curr -= amount 
    if line.startswith("R"):
        curr += amount 

    curr %= 100

    if curr == 0:
        solution += 1

print(solution)
