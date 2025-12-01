lines = []

with open("input.txt", 'r') as f:
    for line in f:
        lines.append(line)


curr = 50
solution = 0
for line in lines:
    amount = int(line[1:])
    for _ in range(amount):
        if line.startswith("L"):
            curr -= 1 
        else:
            curr += 1 
        curr %= 100
        if curr == 0:
            solution += 1

print(solution)
