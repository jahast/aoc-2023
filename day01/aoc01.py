with open("input.txt", "r") as f:
    raw = f.readlines()
    chars = [list(line.strip()) for line in raw]

numbers = []

for line in chars:
    digits = [d for d in line if d.isdigit()]
    number = digits[0] + digits[-1]
    numbers.append(int(number))

ans1 = sum(numbers)

print(ans1)

with open("input.txt", "r") as f:
    raw = f.readlines()
    lines = [line.strip() for line in raw]

number_strings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

numbers = []

def safe_index(str, substr):
    try:
        return str.index(substr)
    except:
        return 10000

def safe_rindex(str, substr):
    try:
        return str.rindex(substr)
    except:
        return -1

for line in lines:

    last = (-1, None)
    first = (10000, None)
    for key, val in number_strings.items():
        first_idx_of_cur = safe_index(line, key)
        last_idx_of_cur = safe_rindex(line, key)

        if last[0] < last_idx_of_cur:
            last = (last_idx_of_cur, val)

        if first[0] > first_idx_of_cur:
            first = (first_idx_of_cur, val)

    for i, val in enumerate(list(line)):
        if val.isdigit():
            if last[0] < i:
                last = (i, val)

            if first[0] > i:
                first = (i, val)

    number = first[1] + last[1]
    numbers.append(int(number))

ans2 = sum(numbers)

print(ans2)