with open("input.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1),
       ]

grid_height = len(grid)
grid_width = len(grid[0])

accessable_rolls = 0

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != '@':
            continue

        adjacent_rolls = 0

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if (0 <= nr < grid_height and 
                0 <= nc < grid_width and 
                grid[nr][nc] == '@'):

                adjacent_rolls += 1

        if adjacent_rolls < 4:
            accessable_rolls += 1

print(accessable_rolls)