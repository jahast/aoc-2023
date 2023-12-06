import re

with open("input.txt", "r") as f:
    lines = f.readlines()

games = []
for i, line in enumerate(lines):

    raw_subsets = line.split(";")
    subsets = []
    for raw_subs in raw_subsets:
        reds = re.search(r"(\d+) red", raw_subs)
        blues = re.search(r"(\d+) blue", raw_subs)
        greens = re.search(r"(\d+) green", raw_subs)
        subset = (
                int(reds.groups()[0]) if reds is not None else 0,
                int(blues.groups()[0]) if blues is not None else 0,
                int(greens.groups()[0]) if greens is not None else 0
            )
        subsets.append(subset)
    
    games.append((i + 1, subsets))

valid_ids = []
for game in games:
    is_valid = True
    for subset in game[1]:
        is_valid = is_valid and subset[0] <= 12 and subset[1] <= 14 and subset[2] <= 13

    if is_valid:    
        valid_ids.append(game[0])

ans1 = sum(valid_ids)

print(ans1)

powers = []

for game in games:
    min_r = max([subset[0] for subset in game[1]])
    min_b = max([subset[1] for subset in game[1]])
    min_g = max([subset[2] for subset in game[1]])

    powers.append(min_r * min_b * min_g)

ans2 = sum(powers)

print(ans2)