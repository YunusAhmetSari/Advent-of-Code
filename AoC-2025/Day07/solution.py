# Day 7 https://adventofcode.com/2025/day/7
import copy

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

grid = [list(line) for line in ls]

# Locate S
start = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
            break

new_grid = copy.deepcopy(grid)
rows = len(grid)
cols = len(grid[0])

# Part 1
current_beams = {start[1]}
split_count = 0
for i in range(start[0], rows):
    next_beams = set()
    
    # Iterate over all beams in the current row
    for col in current_beams:
        if not (0 <= col < cols):
            continue
            
        char = grid[i][col]
        
        if char == "S": # Start
            next_beams.add(col)
        elif char == ".": # Pass through
            new_grid[i][col] = "|"
            next_beams.add(col)
        elif char == "^": # Splitter
            if col - 1 >= 0: # Left
                new_grid[i][col-1] = "|"
                next_beams.add(col - 1)
            if col + 1 < cols: # Right
                new_grid[i][col+1] = "|"
                next_beams.add(col + 1)
            split_count += 1
    # Update next row
    current_beams = next_beams
    if not current_beams:
        break

# Print grid
for row in new_grid:
    print("".join(row))

print("Split Count:", split_count)

# Part 2
current_timelines = {start[1]: 1}
for i in range(start[0], rows):
    next_timelines = {}
    
    # Iterate over all timelines in the current row
    for col, count in current_timelines.items():
        if not (0 <= col < cols):
            continue
            
        char = grid[i][col]
        
        if char == "S" or char == ".": # Start or Pass through
            if col in next_timelines:
                next_timelines[col] += count
            else:
                next_timelines[col] = count      
        elif char == "^": # Splitter
            if col - 1 >= 0: # Left
                left_col = col - 1
                if left_col in next_timelines:
                    next_timelines[left_col] += count
                else:
                    next_timelines[left_col] = count
            if col + 1 < cols: # Right
                right_col = col + 1
                if right_col in next_timelines:
                    next_timelines[right_col] += count
                else:
                    next_timelines[right_col] = count

    # Update next row
    current_timelines = next_timelines

# Print total timelines
total_timelines = sum(current_timelines.values())
print("Total Timelines:", total_timelines)