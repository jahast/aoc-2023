with open("input.txt", "r") as f:
    lines = f.readlines()

card_to_num = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

hands = []
for line in lines:
    cards_raw, bid_raw = line.split(" ")
    cards = [int(s) if s.isdigit() else int(card_to_num[s]) for s in cards_raw]
    bid = int(bid_raw)
    hands.append((cards, bid))

def group(cards):
    grouped = {}

    for card in cards:
        if card in grouped:
            grouped[card] += 1
        else:
            grouped[card] = 1
    
    return grouped

scored = []

for hand in hands:
    
    grouped = group(hand[0])

    #five of a kind
    if len(grouped.keys()) == 1:
        score = 8 * 10**15
    #four of a kind
    elif len(grouped.keys()) == 2 and 4 in grouped.values():
        score = 7 * 10**15
    #full house
    elif len(grouped.keys()) == 2:
        score = 6 * 10**15
    #three of a kind
    elif len(grouped.keys()) == 3 and 3 in grouped.values():
        score = 5 * 10**15
    #two pairs
    elif len(grouped.keys()) == 3:
        score = 4 * 10**15
    #one pair
    elif len(grouped.keys()) == 4:
        score = 3 * 10**15
    #high card
    else:
        score = 2 * 10**15

    for i, card in enumerate(hand[0]):
        score += card * 10**(13-i*2)
    
    scored.append((hand[0], hand[1], score))


scored.sort(key=lambda x: x[2])

ans1 = sum([(i + 1) * hand[1] for i, hand in enumerate(scored)])

print(ans1)

#lazy copy-paste

card_to_num = {
    "T": 10,
    "J": 0,
    "Q": 12,
    "K": 13,
    "A": 14
}

hands = []
for line in lines:
    cards_raw, bid_raw = line.split(" ")
    cards = [int(s) if s.isdigit() else int(card_to_num[s]) for s in cards_raw]
    bid = int(bid_raw)
    hands.append((cards, bid))


def reallocate_js(grouped: dict):

    js = grouped.pop(0, None)

    if len(grouped) == 0:
        return {0: 5}

    if js != None:
        max_key, max_val = 0,0

        for key, val in grouped.items():
            if val > max_val:
                max_key, max_val = key, val
        
        grouped[max_key] += js

    return grouped

scored = []

for hand in hands:
    
    grouped = group(hand[0])
    grouped = reallocate_js(grouped)

    #five of a kind
    if len(grouped.keys()) == 1:
        score = 8 * 10**15
    #four of a kind
    elif len(grouped.keys()) == 2 and 4 in grouped.values():
        score = 7 * 10**15
    #full house
    elif len(grouped.keys()) == 2:
        score = 6 * 10**15
    #three of a kind
    elif len(grouped.keys()) == 3 and 3 in grouped.values():
        score = 5 * 10**15
    #two pairs
    elif len(grouped.keys()) == 3:
        score = 4 * 10**15
    #one pair
    elif len(grouped.keys()) == 4:
        score = 3 * 10**15
    #high card
    else:
        score = 2 * 10**15

    for i, card in enumerate(hand[0]):
        score += card * 10**(13-i*2)
    
    scored.append((hand[0], hand[1], score))

scored.sort(key=lambda x: x[2])

ans2 = sum([(i + 1) * hand[1] for i, hand in enumerate(scored)])

print(ans2)