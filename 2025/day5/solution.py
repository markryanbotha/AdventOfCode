with open("input.txt", "r") as f:
    ranges = [] 
    ingredients = []
    for line in f: 
        if "-"  in line:
           key, value = line.strip().split('-')
           ranges.append((int(key), int(value)))
        elif line.strip() != "":
            ingredients.append(int(line.strip()))


solution = 0
for ingredient in ingredients:
    used = False
    for key, value in ranges:
        if value >= ingredient >= key and not used:
            used = True
            solution += 1
print(solution)
