import re
import functools

with open("input.txt", "r") as f:
    raw = f.readlines()
    lines = [line.strip() for line in raw if line.strip() != ""]

seeds = [int(n) for n in re.findall(r"\d+", lines[0])]

def red(acc, el):
    if "map" in el:
        acc.append([])
    else:
        map = [int(n) for n in re.findall(r"\d+", el)]
        acc[-1].append(map)
    
    return acc

maps = functools.reduce(red, lines[1:], [])

mapped = []

for seed in seeds:
    cur = seed

    for map in maps:
        for submap in map:
            delta = cur - submap[1]
            if delta >= 0 and delta <= submap[2]:
                cur = submap[0] + delta
                break
    
    mapped.append(cur)

ans1 = min(mapped)

print(ans1)

interest_points = []

seed_sets = seeds / 2

for i in range(0, seed_sets, 2):
    seed_start, seed_range = seeds[i:i+1]
    