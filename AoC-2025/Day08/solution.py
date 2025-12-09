with open("input.txt") as f:
    ls = f.read().strip().split("\n")

# Parse points
points = []
for line in ls:
    parts = line.split(',')
    points.append([int(parts[0]), int(parts[1]), int(parts[2])])

# Part 1
# Find distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]
        dist = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
        distances.append([dist, i, j])

distances.sort() # Sort distances
groups = list(range(len(points))) # Initialize groups

# Union-Find
for k in range(len(points)):
    dist, idx1, idx2 = distances[k]
    
    group_id_1 = groups[idx1]
    group_id_2 = groups[idx2]
    
    if group_id_1 != group_id_2:
        for i in range(len(groups)):
            if groups[i] == group_id_2:
                groups[i] = group_id_1

# Count groups
counts = {}
for g_id in groups:
    if g_id not in counts:
        counts[g_id] = 0
    counts[g_id] += 1

# Get sizes of groups
sizes = sorted(list(counts.values()), reverse=True)
print("Part 1 Answer:", sizes[0] * sizes[1] * sizes[2])

# Part 2
# Reset groups
groups = list(range(len(points)))
num_groups = len(points)

# Iterate through all distances
for dist, idx1, idx2 in distances:
    group_id_1 = groups[idx1]
    group_id_2 = groups[idx2]
    
    if group_id_1 != group_id_2:
        for i in range(len(groups)):
            if groups[i] == group_id_2:
                groups[i] = group_id_1
        num_groups -= 1
        if num_groups == 1:
            x1 = points[idx1][0]
            x2 = points[idx2][0]
            print("Part 2 Answer:", x1 * x2)
            break