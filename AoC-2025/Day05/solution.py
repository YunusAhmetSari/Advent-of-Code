# Day 5 https://adventofcode.com/2025/day/5

with open("input.txt") as f:
    ls_ranges, ls_ids = f.read().strip().split("\n\n")

ls_ranges = list(ls_ranges.split("\n"))
ls_ids = list(ls_ids.split("\n"))

# Part 1 - Fresh ingredients based on ranges and ids
count_fresh = 0
for i in ls_ids:
    # Check if i is in the range of ls_ranges
    for j in ls_ranges:
        if int(i) in range(int(j.split("-")[0]), int(j.split("-")[1]) + 1):
            count_fresh += 1
            break

print("Fresh ingredients by ids in ranges:", count_fresh)

# Part 2 - Fresh ingredients based on ranges only
# Parse ranges
parsed_ranges = []
for i in ls_ranges:
    start, end = map(int, i.split("-"))
    parsed_ranges.append((start, end))

# Sort by start time
parsed_ranges.sort(key=lambda x: x[0])

# Merge ranges
merged_ranges = []
for start, end in parsed_ranges:
    if not merged_ranges:
        merged_ranges.append((start, end))
    else:
        last_start, last_end = merged_ranges[-1]
        # Check for overlap or adjacency
        if start <= last_end + 1:
            merged_ranges[-1] = (last_start, max(last_end, end))
        else:
            merged_ranges.append((start, end))

# Count total elements
count_fresh = 0
for start, end in merged_ranges:
    count_fresh += end - start + 1

print("Fresh ingredients by ranges:", count_fresh)