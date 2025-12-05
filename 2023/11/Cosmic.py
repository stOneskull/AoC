expansion = 1_000_000

with open("input.txt", "r") as file:
    rows = file.readlines()

grid = [row.strip() for row in rows]

grid_height = len(grid)
grid_width = len(grid[0])


empty_rows = set()

for r, row in enumerate(grid):
    if '#' not in row:
        empty_rows.add(r)

empty_cols = set()

for c in range(grid_width):
    if not any(grid[r][c] == '#' for r in range(grid_height)):
        empty_cols.add(c)

galaxies = []

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == '#':
            galaxies.append((r, c))


total_distance = 0

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        g1_r, g1_c = galaxies[i]
        g2_r, g2_c = galaxies[j]

        r1, r2 = min(g1_r, g2_r), max(g1_r, g2_r)
        c1, c2 = min(g1_c, g2_c), max(g1_c, g2_c)

        dist = (r2 - r1) + (c2 - c1)

        for r in range(r1, r2):
            if r in empty_rows:
                dist += expansion-1

        for c in range(c1, c2):
            if c in empty_cols:
                dist += expansion-1
        
        total_distance += dist


print(total_distance)
