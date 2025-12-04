ranges = []

with open("input.txt", 'r') as f:
    ranges_string = f.read().strip().split(",")
    for r in ranges_string:
        start, end = r.split("-")
        ranges.append((int(start), int(end)))

solution = 0

for rg in ranges:
    for i in range(rg[0], rg[1]):
        sNum = str(i)
        midpoint = len(sNum) // 2
        if sNum[:midpoint] == sNum[midpoint:]:
            solution += i

print(solution)

