# Day 2 https://adventofcode.com/2025/day/2

with open("input.txt") as f:
    ls = f.read().strip().split(",")

invalid_id_1 = 0
invalid_id_2 = 0

for i in ls:
    start, end = i.split("-")
    for j in range(int(start), int(end) + 1):
        s = str(j)
        mid = len(s) // 2
        # Part 1 - Sequence of digits repeated twice
        if len(s) % 2 == 0 and s[:mid] == s[mid:]: 
            invalid_id_1 += j
        # Part 2 - Sequence of digits repeated at least twice
        for k in range(1, mid + 1):
            if s == s[:k] * (len(s) // k):
                invalid_id_2 += j
                break
            
print(invalid_id_1)
print(invalid_id_2)