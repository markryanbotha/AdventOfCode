with open("input.txt", 'r') as f:
    arr = [list(line.strip()) for line in f]

def inBounds(dx, x, dy, y):
    return 0 <= dx + x < len(arr[0]) and 0 <= dy + y < len(arr)

def search(x, y, seen):
    directions = [(0, -1), (1, 0), (-1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dx, dy in directions:
        if inBounds(dx, x, dy, y) and arr[y + dy][x + dx] == "@":
            seen += 1
    return seen


solution = 0
for y, row in enumerate(arr):
    for x in range(len(row)):
        if arr[y][x] != "@":
            continue
        seen = search(x, y, 0)
        if seen < 4:
            print(f"x: {x}, y: {y}")
            solution += 1


print(solution)



