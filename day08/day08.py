import re
import math
import itertools
import functools

with open("input.txt", "r") as f:
    raw = f.readlines()
    lines = [line.strip() for line in raw]

dirs = [n for n in lines[0]]
dirs_len = len(dirs)

network = {}

for line in lines[2:]:
    points = [p for p in re.findall(r"[A-Z]{3}", line)]
    network[points[0]] = { "L": points[1], "R": points[2] }

i = 0
cur = "AAA"

while True:
    if cur == "ZZZ":
        break
    dir = dirs[i % dirs_len]
    cur = network[cur][dir]
    i += 1

ans1 = i

print(ans1)

curs = [k for k in network.keys() if k[2] == "A"]

first_hits = []

for cur in curs:
    i = 0
    while True:
        if cur[2] == "Z":
            first_hits.append(i)
            break
        dir = dirs[i % dirs_len]
        cur = network[cur][dir]
        i += 1

def lcm(a,b):
    return abs(a*b) // math.gcd(a,b)

ans2 = functools.reduce(lambda x, y: lcm(x,y), first_hits)

print(ans2)
