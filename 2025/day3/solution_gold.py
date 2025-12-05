with open('input.txt', 'r') as f:
    banks = [line.strip() for line in f]

def max_joltage(bank):
    to_skip = len(bank) - 12
    stack = []

    for digit in bank:
        # Remove smaller digits when a bigger one arrives (greedy max)
        # Stop removing once we've reached our limit (remaining number of digits is 12)
        while stack and to_skip > 0 and stack[-1] < digit:
            stack.pop()
            to_skip -= 1
        stack.append(digit)

    return int(''.join(stack[:12]))

solution = sum([max_joltage(bank) for bank in banks])
print(solution)

