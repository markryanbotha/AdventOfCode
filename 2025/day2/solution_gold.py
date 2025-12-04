ranges = []

with open("input.txt", 'r') as f:
    rangesString = f.read().strip().split(",")
    for r in rangesString:
        start, end = r.split("-")
        ranges.append((int(start), int(end)))

solution = 0

def isInvalid(num):
    s = str(num)
    n = len(s)
    # Try all possible pattern lengths from 1 to half the string length
    # as patterns longer than half can't repeat at least twice
    for patternLen in range(1, n // 2 + 1):
        # Only check if the pattern length divides evenly into the total length
        if n % patternLen == 0:
            pattern = s[:patternLen]
            # Check if repeating this pattern recreates the full number
            # If it ever does, then you know it's invalid
            if pattern * (n // patternLen) == s:
                return True
    return False


for rg in ranges:
    for i in range(rg[0], rg[1] + 1):
        if isInvalid(i):
            solution += i


print(solution)

