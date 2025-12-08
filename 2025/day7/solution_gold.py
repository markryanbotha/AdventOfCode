with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f]

def printOut(lines):
    for line in lines:
        print("".join(line))

solution = 0
# Constructing final state
for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char == 'S':
            lines[j][i] = '|'
        elif lines[j][i] == '^' and lines[j-1][i] == "|":
            lines[j][i-1] = '|'
            lines[j][i+1] = '|'
        elif lines[j-1][i] == '|':
            lines[j][i] = '|'

# Starting from the bottom of the completed state 
# we trace back up every possibile beam ("|"), if we the next row directly above is not a beam
# look left / right at next row to find if there is a splitter
# for the splitter, take each path up (left and right) 
# base case is if we reach the end of the lines 
# reversing to make it easier to step forward
lines.reverse()

# Use memoization (otherwise painfully painfully slow) 
memo = {}

def traceBack(rIndex, cIndex):
    if (rIndex, cIndex) in memo:
        return memo[(rIndex, cIndex)]

    if rIndex == len(lines) - 1:
        return 1
    total = 0
    if lines[rIndex + 1][cIndex] == '|':
        total += traceBack(rIndex+1, cIndex)
    if cIndex > 0 and lines[rIndex][cIndex-1] == '^':
        total += traceBack(rIndex+1, cIndex-1)
    if cIndex < len(lines[0]) - 1 and lines[rIndex][cIndex+1] == '^':
        total += traceBack(rIndex+1, cIndex+1)

    memo[(rIndex, cIndex)] = total
    return total


# Traceback from each start point at the bottom that received a ray 
solution = sum(traceBack(0, i) for i, char in enumerate(lines[0]) if char == "|")
print(solution)
