# Day 1 https://adventofcode.com/2025/day/1

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

# Part 1 - Moves dial in rotations
dial = 50 # start position
count = 0 # count rotations

for i in ls:
    direction, rotate = i[0], int(i[1:])
    if direction == "L":
        dial -= rotate
    else:
        dial += rotate
    
    dial %= 100
    if dial == 0:
        count += 1

print(count)

# Part 2 - Moves dial in steps
dial = 50 # start position
count = 0 # count rotations

for i in ls:
    direction, rotate = i[0], int(i[1:])
    for _ in range(rotate):
        if direction == "L":
            dial -= 1
        else:
            dial += 1
    
        dial %= 100
        if dial == 0:
            count += 1

print(count)