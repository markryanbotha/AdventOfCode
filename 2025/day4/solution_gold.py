with open("input.txt", 'r') as f:
    arr = [list(line.strip()) for line in f]

def inBounds(dx, x, dy, y):
    return 0 <= dx + x < len(arr[0]) and 0 <= dy + y < len(arr)

def search(x, y, seen, arr):
    directions = [(0, -1), (1, 0), (-1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dx, dy in directions:
        if inBounds(dx, x, dy, y) and arr[y + dy][x + dx] == "@":
            seen += 1
    return seen


# Repeat the solution from step one if a roll is ever removed
# not sure why counting as you go doesn't work, but marking removal with x 
def round(arr):
    didRemove = False
    newArr = arr
    for y, row in enumerate(arr):
        for x in range(len(row)):
            if arr[y][x] != "@":
                continue
            seen = search(x, y, 0, arr)
            if seen < 4:
                didRemove = True
                newArr[y][x] = 'x'
    if didRemove:
        output = ""
        round(newArr) 
    return newArr 


newArr = round(arr)

# Counting number of x's at the end
solution = 0
for y, row in enumerate(newArr):
    for x in range(len(row)):
        if newArr[y][x] == 'x':
            solution += 1

print(solution)

