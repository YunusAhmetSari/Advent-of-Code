# Day 4 https://adventofcode.com/2025/day/4
import copy

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

# Adding . around input
grid = [list("." + line + ".") for line in ls]
width = len(grid[0])
grid.insert(0, ["."] * width)
grid.append(["."] * width)

rows = len(grid)
cols = len(grid[0])

# Copy to handle visualization
while True:
    new_grid = copy.deepcopy(grid)
    changed = False

    # Iterate over the grid (exclude borders)
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            count = 0
            # Check all 8 neighbors
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    if grid[y + dy][x + dx] == "@":
                        count += 1
            
            # If current is @ and neighbors < 4, change to X
            if grid[y][x] == "@" and count < 4:
                new_grid[y][x] = "X"
                changed = True
    
    grid = new_grid
    if not changed:
        break

# Print grid
for row in grid:
    print("".join(row))

# Count all "X" in grid
counts = 0
for row in grid:
    counts += row.count("X")
print(counts)