import re

with open("input.txt", "r") as f:
    raw = f.readlines()

lines = []

for line in raw:
    line_as_numbers = [int(n) for n in re.findall(r"-?\d+", line)]
    lines.append(line_as_numbers)

def differences(ls: "list[int]"):
    diff = []
    for i in range(0, len(ls) - 1):
        diff.append(ls[i+1] - ls[i])
    return diff

ans1 = 0
lasts = []

for line in lines:
    sub_lasts = [line[-1]]
    diffs = line
    while True:
        diffs = differences(diffs)
        sub_lasts.append(diffs[-1])
        if not any(diffs):
            break
    lasts.append(sum(sub_lasts))

ans1 = sum(lasts)
print(ans1)

lasts = []

for line in lines:
    last_diffs = [line[0]]
    diffs = line
    while True:
        diffs = differences(diffs)
        last_diffs.append(diffs[0])
        if not any(diffs):
            break

    last_diffs.reverse()

    sub_lasts = [0]
    for i in range(0, len(last_diffs)):
        nxt = last_diffs[i] - sub_lasts[i]
        sub_lasts.append(nxt)


    lasts.append(sub_lasts[-1])

ans2 = sum(lasts)
print(ans2)