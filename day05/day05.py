import re
import functools
import itertools

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

# (range_start, range_end, delta)
ranges = []
for i in range(0, len(seeds), 2):
    ranges.append(seeds[i], seeds[i+1], 0)


from_start_to_end = [mapped[i] for i in range(0, len(seeds), 2)]

for i in range(len(maps) - 1, -1, -1):
    for submap in maps[i]:
        candidates = [submap[0] - 1, submap[0], submap[0] + submap[2] - 1]



# for map in maps:
#     new_ranges = []
#     for range in ranges:
#         mapped_range_start, mapped_range_end = range[0] + range[2] - 1, range[1] + range[2] - 1
#         for submap in map:
#             submap_range_start, submap_range_end = submap[1], submap[1] + submap[2] - 1
#             submap_delta = submap[0] - submap[1]

#             start_delta = mapped_range_start - submap_range_start
#             end_delta = mapped_range_end - submap_range_end

#             # no overlap
#             if start_delta < 0 and 0 < end_delta:
#                 continue
#             # range is included in submap
#             elif start_delta > 0 and 0 < end_delta:
#                 new_ranges.append(range[0], range[0] + start_delta - 1, range[2])
#                 new_ranges.append(range[0] + start_delta, range[0] + start_delta + submap[2] - 1, range[2] + submap_delta)
#                 new_ranges.append(range[0] + start_delta + submap[2], range[1], range[2])
#                 continue
#             elif start_delta > 0 and 0 > end_delta:
#                 new_ranges.append(range[0], range[0] + start_delta - 1, range[2])
#                 new_ranges.append(range[0] + start_delta, range[1], range[2] + submap_delta)
#                 continue
#             elif start_delta < 0 and 0 > end_delta:
#                 new_ranges.append(range[0], range[0] + start_delta - 1, range[2])
#                 continue
