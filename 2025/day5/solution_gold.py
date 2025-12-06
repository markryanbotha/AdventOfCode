with open("input.txt", "r") as f:
    ranges = [] 
    for line in f: 
        if "-"  in line:
           key, value = line.strip().split('-')
           ranges.append((int(key), int(value)))

# I tried the below, but the ranges are too big :/ need to think of a more efficient solution
# seen = set()
# for key, value in ranges:
#     for i in range(key, value+1):
#         seen.add(i)
# solution = len(seen)
# print(solution)

# Sort ranges (this will do it by first element of tuple, then the second if they're the same)
# This allows us to compare adjacent ranges
ranges.sort()
merged = []
for l, r in ranges:
    # Check if current range overlaps the previous merged range
    if merged and l <= merged[-1][1]:
        prevL, prevR = merged[-1]
        # Extend the last merged range to include current range
        # Get maximum r value incases previous range extends further than current one 
        merged[-1] = (prevL, max(prevR, r))
    else:
        # Ranges did not overlap, add as a new non-overlapping range
        merged.append((l, r))

# Get the difference (inclusive) of each range to see how many valid ingredients there are
solution = sum(r - l + 1 for l, r in merged)
print(solution)


