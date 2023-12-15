with open("test.txt", "r") as f:
    raw = f.readlines()
    lines = [line.strip() for line in raw]

links = {}

def encode(i: int, j: int):
    return f"{i}_{j}"

def neighbors(i: int,j: int, char: str):
    here  = encode(i, j)
    north = encode(i - 1, j)
    south = encode(i + 1, j)
    west  = encode(i, j - 1)
    east  = encode(i, j + 1)

    if char == "|":
        return {here: [north, south]}
    elif char == "-":
        return {here: [west, east]}
    elif char == "L":
        return {here: [north, east]}
    elif char == "J":
        return {here: [west, north]}
    elif char == "7":
        return {here: [west, south]}
    elif char == "F":
        return {here: [south, east]}
    else:
        return None


for i, line in enumerate(lines):
    for j, char in enumerate(line):
        print(i,j,char)