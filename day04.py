import re

with open("input.txt", "r") as f:
    lines = f.readlines()

games = []

for line in lines:
    _, numbers = line.strip().split(":")
    winning_numbers_str, my_numbers_str = numbers.split("|")
    winning_numbers = [int(n) for n in re.findall(r"\d+", winning_numbers_str)]
    my_numbers = [int(n) for n in re.findall(r"\d+", my_numbers_str)]
    games.append((winning_numbers, my_numbers))

ans1 = 0

for game in games:
    intersect = set(game[0]).intersection(set(game[1]))
    matching_numbers_n = len(intersect)
    if matching_numbers_n > 0:
        ans1 += 2**(matching_numbers_n-1)

print(ans1)

cards = [1 for _ in range(0, len(games))]

for i, game in enumerate(games):
    intersect = set(game[0]).intersection(set(game[1]))
    matching_numbers_n = len(intersect)

    for j in range(i + 1, i + matching_numbers_n + 1):
        cards[j] = cards[j] + cards[i]

ans2 = sum(cards)

print(ans2)