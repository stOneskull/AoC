with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1),
       ]

grid_height = len(grid)
grid_width = len(grid[0])

removed_rolls = 0

while True:
    remove = []

    for r in range(grid_height):
        for c in range(grid_width):
            if grid[r][c] != '@':
                continue

            adjacent_rolls = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (0 <= nr < grid_height and 
                    0 <= nc < grid_width and 
                    grid[nr][nc] == '@'):
                    adjacent_rolls += 1
            
            if adjacent_rolls < 4:
                remove.append((r, c))

    if not remove:
        break

    for r, c in remove:
        grid[r][c] = '.'
        
    removed_rolls += len(remove)


print(removed_rolls)