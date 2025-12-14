import re
from itertools import combinations

data = []
# Convert the desired outcome into bits, and each combo into bit representation
with open("input.txt", "r") as f:
    for line in f:
        bracket = re.findall(r'\[([^\]]*)\]', line)[0]
        desired = ""
        for char in bracket:
            if char == '#':
                desired += '1'
            else:
                desired += '0'
        parens = re.findall(r'\(([^)]*)\)', line)
        combos = [n.split(",") for n in parens]
        options = []
        for i in range(len(combos)):
            option = "".zfill(len(desired))
            for j in range(len(combos[i])):
                spot = int(combos[i][j])
                option = option[:spot] + '1' + option[spot+1:]
            options.append(int(option, 2))

        data.append((int(desired, 2), options))


def minPresses(target, buttons):
    n = len(buttons)
    # Try num presses 1, 2, 3, 4 ext. up to clicking all buttons
    for size in range(n + 1):
        # combinations is really handly, returns all combinations of list
        # where each element is size length
        for combo in combinations(buttons, size):
            result = 0
            # We are doing XOR operations, mimics pressing on/off
            for button in combo:
                result ^= button
            if result == target:
                return size

    raise Exception("There was no solution, this shouldn't have happened")


solution = 0
for target, buttons in data:
    solution += minPresses(target, buttons)

print(solution)
