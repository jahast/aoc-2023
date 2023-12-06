import re

with open("input.txt", "r") as f:
    lines = f.readlines()

all_numbers = []
all_symbols = []
for i, line in enumerate(lines):
    numbers = [(i, m.start(), m.end() - 1, int(m.group(0))) for m in re.finditer(r"\d+", line)]
    all_numbers.extend(numbers)

    sybmols = [(i, m.start(), m.group(0)) for m in re.finditer(r"[^\d\.]", line.strip())]
    all_symbols.extend(sybmols)

next_to_symbol = []
for symbol in all_symbols:
    on_correct_row = [n for n in all_numbers if abs(n[0] - symbol[0]) <= 1]
    nearby = [n for n in on_correct_row if abs(n[1] - symbol[1]) <= 1 or abs(n[2] - symbol[1]) <= 1]
    next_to_symbol.extend(nearby)

uniques = set(next_to_symbol)
nearby_numbers = [ n[3] for n in list(uniques) ]

ans1 = sum(nearby_numbers)

print(ans1)

potential_gears = [s for s in all_symbols if s[2] == "*"]

gear_ratios = []

for symbol in potential_gears:
    on_correct_row = [n for n in all_numbers if abs(n[0] - symbol[0]) <= 1]
    nearby = [n for n in on_correct_row if abs(n[1] - symbol[1]) <= 1 or abs(n[2] - symbol[1]) <= 1]

    if len(nearby) == 2:
        gear_ratios.append(nearby[0][3] * nearby[1][3])

ans2 = sum(gear_ratios)

print(ans2)