from collections import defaultdict

banks = []


with open("input.txt", 'r') as f:
    for line in f:
        banks.append(line.strip())


solution = 0


for bank in banks:
    l, r = 0, 0
    for i, battery in enumerate(bank):
        numBatteries = len(bank) - 1
        battery = int(battery)
        # Always update left battery to highest number, if it isn't the last battery in the bank
        if l < battery and i < numBatteries:
            l = battery
            r = 0
        # Otherwise, update right battery if left can't be improved
        elif r < battery:
            r = battery
    solution += int(str(l) + str(r))

print(solution)



