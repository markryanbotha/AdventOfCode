from collections import defaultdict
from functools import lru_cache

graph = defaultdict(list)

with open("input.txt", "r") as f:
    for line in f:
        input, output = line.strip().split(":")
        for device in output.split(" "):
            if len(device) > 0:
                graph[input].append(device)


@lru_cache(maxsize=None)
def dfs(start, has_fft, has_dac):
    if start == 'out':
        return 1 if has_fft and has_dac else 0
    return sum(dfs(device, has_fft or device == 'fft',
                   has_dac or device == 'dac') for device in graph[start])


print(dfs('svr', False, False))
