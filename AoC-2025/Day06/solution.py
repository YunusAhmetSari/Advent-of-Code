# Day 6 https://adventofcode.com/2025/day/6

from math import prod

with open("input.txt") as f:
    ls = f.readlines()

# Part 1
grid = []   
for line in ls:
    row = line.split()
    grid.append(row)

sum_list = []
# Based on last row add/multiply all values in the same column
for i in range(len(grid[0])):
    if grid[-1][i] == "+":
        sum_list.append(sum(int(x[i]) for x in grid[:-1]))
    elif grid[-1][i] == "*":
        sum_list.append(prod(int(x[i]) for x in grid[:-1]))

print("Part 1:", sum(sum_list))

# Part 2
with open("input.txt") as f:
    raw_lines = f.readlines()

# Clean and pad lines
lines = [line.rstrip('\n') for line in raw_lines]
max_len = max(len(line) for line in lines) if lines else 0
padded_lines = [line.ljust(max_len) for line in lines]

row_lines = padded_lines[:-1]
op_line = padded_lines[-1]

# Identify blocks based on empty columns
blocks = []
in_block = False
start = 0
for i in range(max_len):
    col_is_empty = all(row[i] == ' ' for row in row_lines)
    if not col_is_empty:
        if not in_block:
            start = i
            in_block = True
    else:
        if in_block:
            blocks.append((start, i))
            in_block = False
if in_block:
    blocks.append((start, max_len))

part2_sum = 0

# Process blocks from Right to Left
for start, end in reversed(blocks):
    # Find operator
    ops = op_line[start:end]
    if "*" in ops:
        is_mult = True
    else:
        is_mult = False
        
    nums = []
    # Process columns Right to Left
    for col_idx in reversed(range(start, end)):
        # Read digits Top to Bottom
        num_str = ""
        for row in row_lines:
            if row[col_idx] != ' ':
                num_str += row[col_idx]
        if num_str:
            nums.append(int(num_str))
            
    # Calculate block result
    if nums:
        if not is_mult:
            part2_sum += sum(nums)
        else:
            part2_sum += prod(nums)

print("Part 2:", part2_sum)