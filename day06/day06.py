import re
import functools
import math

with open("input.txt", "r") as f:
    lines = f.readlines()

times = [int(n) for n in re.findall(r"\d+", lines[0])]
dists = [int(n) for n in re.findall(r"\d+", lines[1])]

total_ways_to_win = []

for i in range(0, len(times)):
    time, dist = times[i], dists[i]

    ways_to_win = 0

    for t in range(1, time + 1):
        cur_dist = t * (time - t)
        if cur_dist > dist:
            ways_to_win += 1
    
    total_ways_to_win.append(ways_to_win)

ans1 = functools.reduce(lambda x,y: x*y, total_ways_to_win, 1)

print(ans1)

time2 = int("".join([n for n in re.findall(r"\d+", lines[0])]))
dist2 = int("".join([n for n in re.findall(r"\d+", lines[1])]))

ans2 = 0

x1 = (-time2 + math.sqrt(time2**2 - 4*(-1)*(-dist2))) / -2
x2 = (-time2 - math.sqrt(time2**2 - 4*(-1)*(-dist2))) / -2

ans2 = math.floor(x2) - math.ceil(x1) + 1

print(ans2)