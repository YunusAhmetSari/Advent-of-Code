# Day 3 https://adventofcode.com/2025/day/3

with open("input.txt") as f:
    ls = f.read().strip().split("\n")


def calculate_sum(data, num_batteries):
    total_sum = 0
    for i in data:
        list_batteries = []
        index = 0
        for j in reversed(range(0, num_batteries)):
            slice_end = len(i) - j
            highest_value = max(i[index:slice_end])
            highest_value_index = i.index(highest_value, index)
            index = highest_value_index + 1
            list_batteries.append(highest_value)
        str_batteries = "".join(list_batteries)
        total_sum += int(str_batteries)
    return total_sum

print(calculate_sum(ls, 2)) # Part 1 - 2 Batteries
print(calculate_sum(ls, 12)) # Part 2 - 12 Batteries