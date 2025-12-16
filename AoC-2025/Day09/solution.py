# Day 9 https://adventofcode.com/2025/day/9

def solve():
    with open("input.txt") as f:
        content = f.read().strip()

    ls = []
    for line in content.split("\n"):
        parts = line.strip().split(",")
        ls.append((int(parts[0]), int(parts[1])))

    # Part 1
    max_area = 0
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            x1, y1 = ls[i]
            x2, y2 = ls[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            max_area = max(max_area, area)

    print(f"Part 1: Max_area = {max_area}")

    # Part 2 - AI generated solution
    # Polygon edges
    N = len(ls)
    edges = []
    for i in range(N):
        p1 = ls[i]
        p2 = ls[(i + 1) % N]
        edges.append((p1, p2))

    def is_inside(x, y):
        # Ray casting algorithm
        # Ray: (x, y) -> (inf, y)
        inside = False
        for p1, p2 in edges:
            x1, y1 = p1
            x2, y2 = p2
            
            # Check edge intersection with ray
            # Edge must span y (one point above, one below)
            # strictly > or >= depends on standard.
            # Standard: (y1 > y) != (y2 > y)
            if ((y1 > y) != (y2 > y)):
                # Intersection x coordinate
                # x_int = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                # Check if x < x_int
                # To avoid division, multiply
                # x < x1 + ... <=> (x - x1) * (y2 - y1) < (y - y1) * (x2 - x1)
                # Be careful with signs if (y2 - y1) is negative
                
                # Let's compute x intersection directly
                inters_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                if x < inters_x:
                    inside = not inside
        return inside

    def rect_intersects_any_edge(rx1, rx2, ry1, ry2):
        # Rectangle Interior: (rx1, rx2) x (ry1, ry2) (exclusive)
        # Check if any edge intersects this region
        # Edge (ux, uy) -> (vx, vy)
        
        # Sort coordinates for bounds
        r_min_x, r_max_x = min(rx1, rx2), max(rx1, rx2)
        r_min_y, r_max_y = min(ry1, ry2), max(ry1, ry2)
        
        for p1, p2 in edges:
            ux, uy = p1
            vx, vy = p2
            
            # Check if edge is vertical
            if ux == vx:
                # Vertical edge at x = ux
                # Intersects if r_min_x < ux < r_max_x
                # AND y-ranges overlap
                if r_min_x < ux < r_max_x:
                    e_min_y, e_max_y = min(uy, vy), max(uy, vy)
                    # Overlap of (e_min, e_max) with (r_min, r_max)
                    # Intersection must have length > 0 within interior
                    # e_max > r_min and e_min < r_max ?
                    # Overlap interval: (max(e_min, r_min), min(e_max, r_max))
                    # Valid if top > bottom
                    common_min_y = max(e_min_y, r_min_y)
                    common_max_y = min(e_max_y, r_max_y)
                    if common_max_y > common_min_y:
                        return True
            
            # Check if edge is horizontal
            elif uy == vy:
                # Horizontal edge at y = uy
                # Intersects if r_min_y < uy < r_max_y
                if r_min_y < uy < r_max_y:
                    e_min_x, e_max_x = min(ux, vx), max(ux, vx)
                    common_min_x = max(e_min_x, r_min_x)
                    common_max_x = min(e_max_x, r_max_x)
                    if common_max_x > common_min_x:
                        return True
        return False

    max_area_p2 = 0
    
    # Iterate all pairs of vertices
    for i in range(N):
        for j in range(i + 1, N):
            p1 = ls[i]
            p2 = ls[j]
            x1, y1 = p1
            x2, y2 = p2
            
            # Optimization: Area must be > current max
            current_area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if current_area <= max_area_p2:
                continue
            
            # Valid rectangle check
            
            # 1. Midpoint check
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            
            if not is_inside(mid_x, mid_y):
                continue
                
            # 2. Edge intersection check
            if rect_intersects_any_edge(x1, x2, y1, y2):
                continue
            
            # If passed, it's valid
            max_area_p2 = current_area

    print(f"Part 2: Max_area = {max_area_p2}")

if __name__ == "__main__":
    solve()