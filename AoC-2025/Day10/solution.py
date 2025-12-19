# Day 10 https://adventofcode.com/2025/day/10

import re

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

def solve_machine(line):
    # [ .##. ] -> target = [0, 1, 1, 0]
    target_str = re.search(r'\[(.*?)\]', line).group(1)
    target = [1 if c == '#' else 0 for c in target_str]
    
    # (0,2) -> button = [1, 0, 1, 0]
    button_strs = re.findall(r'\((.*?)\)', line)
    buttons = []
    for b in button_strs:
        mask = [0] * len(target)
        for idx in b.split(','):
            mask[int(idx)] = 1
        buttons.append(mask)

    # Search for solution
    num_buttons = len(buttons)
    min_presses = float('inf')
    
    for i in range(1 << num_buttons):
        current_state = [0] * len(target)
        press_count = 0
        for b_idx in range(num_buttons):
            if (i >> b_idx) & 1:
                press_count += 1
                # XOR button into current state
                for l_idx in range(len(target)):
                    current_state[l_idx] ^= buttons[b_idx][l_idx]
        
        if current_state == target:
            min_presses = min(min_presses, press_count)
            
    return min_presses

# Part 1
Total = sum(solve_machine(m) for m in ls)
print(f"Part 1: Total = {Total}")