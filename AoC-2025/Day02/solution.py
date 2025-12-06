# Day 2 https://adventofcode.com/2025/day/2

with open("input.txt") as f:
    ls = f.read().strip().split(",")

invalid_id_1 = 0
invalid_id_2 = 0

for l in ls:
    start, end = l.split("-")
    for i in range(int(start), int(end) + 1):
        s = str(i)
        mid = len(s) // 2
        # Part 1 - Sequence of digits repeated twice
        if len(s) % 2 == 0 and s[:mid] == s[mid:]: 
            invalid_id_1 += i
        # Part 2 - Sequence of digits repeated at least twice
        for l in range(1, mid + 1):
            if s == s[:l] * (len(s) // l):
                invalid_id_2 += i
                break
            
print(invalid_id_1)
print(invalid_id_2)