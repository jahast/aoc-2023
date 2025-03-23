import re
import functools
import sys

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
            if delta >= 0 and delta <= (submap[2] - 1):
                cur = submap[0] + delta
                break
    
    mapped.append(cur)

ans1 = min(mapped)

print(ans1)

breakpoints = []
for map in maps[::-1]:
    new_breakpoints = []

    for submap in map:
        new_breakpoints.append(submap[1] - 1)
        new_breakpoints.append(submap[1])
        new_breakpoints.append(submap[1] + 1)

        new_breakpoints.append(submap[1] + submap[2] - 1)
        new_breakpoints.append(submap[1] + submap[2])
        new_breakpoints.append(submap[1] + submap[2] + 1)

    for breakpoint in breakpoints:
        for submap in map:
            delta = breakpoint - submap[0]
            if delta >= 0 and delta <= (submap[2] - 1):
                new_breakpoints.append(submap[1] + delta - 1)
                new_breakpoints.append(submap[1] + delta)
                new_breakpoints.append(submap[1] + delta + 1)
                break
        else:
            new_breakpoints.append(breakpoint - 1)
            new_breakpoints.append(breakpoint)
            new_breakpoints.append(breakpoint + 1)

    breakpoints = new_breakpoints

limits = []
for i in range(0, len(seeds), 2):
    breakpoints.append(seeds[i])
    breakpoints.append(seeds[i] + 1)
    breakpoints.append(seeds[i] + seeds[i+1] - 1)
    breakpoints.append(seeds[i] + seeds[i+1] - 2)
    limits.append((seeds[i],seeds[i] + seeds[i+1] - 1))

seeds_to_try = []
for breakpoint in breakpoints:
    for limit in limits:
        if limit[0] <= breakpoint <= limit[1]:
            seeds_to_try.append(breakpoint)
            break

ans2 = sys.maxsize
for seed in seeds_to_try:
    cur = seed

    for map in maps:
        for submap in map:
            delta = cur - submap[1]
            if delta >= 0 and delta <= (submap[2] - 1):
                cur = submap[0] + delta
                break
    
    ans2 = min(cur, ans2)

print(ans2)
