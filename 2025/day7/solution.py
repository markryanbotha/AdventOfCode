with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f]

def printOut():
    for line in lines:
        print("".join(line))

solution = 0
for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char == 'S':
            lines[j][i] = '|'
        elif lines[j][i] == '^' and lines[j-1][i] == "|":
            lines[j][i-1] = '|'
            lines[j][i+1] = '|'
            solution += 1
        elif lines[j-1][i] == '|':
            lines[j][i] = '|'
    printOut()
    print("\n\n")

# solution = 0
# for char in lines[-1]:
#     if char == '|':
#         solution += 1

print(solution)
