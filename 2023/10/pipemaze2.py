with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

grid_height, grid_width = len(lines), len(lines[0])

for row_num, row in enumerate(lines):
    for col_num, char in enumerate(row):
        if char == "S":
            start_row = row_num
            start_col = col_num
            break
    if char == "S":
        break


dirs = {
    'N': (-1, 0), 
    'S': (1, 0), 
    'W': (0, -1), 
    'E': (0, 1),
}

n, s, w, e = dirs.values()


pipes = {
    '|': (n, s),
    '-': (w, e),
    'L': (n, e),   
    'J': (n, w),
    '7': (w, s),
    'F': (s, e),
}


S_connections = set()

for _, (dir_row, dir_col) in dirs.items():
    next_row = start_row + dir_row
    next_col = start_col + dir_col
    opposite_dir = (-dir_row, -dir_col)

    if not (0 <= next_row < grid_height and 
            0 <= next_col < grid_width):
        continue
    
    next_pipe = lines[next_row][next_col]

    if (next_pipe in pipes and 
        opposite_dir in pipes[next_pipe]):

        S_connections.add((dir_row, dir_col))


S_pipe = 'S' 

for pipe, pipe_connections in pipes.items():
    if S_connections == set(pipe_connections):
        S_pipe = pipe
        break


lines[start_row] = (
    lines[start_row][:start_col] 
    + S_pipe + 
    lines[start_row][start_col+1:]
)


path = {(start_row, start_col)}

for dir_row, dir_col in (n, s, w, e):
    next_row = start_row + dir_row
    next_col = start_col + dir_col

    if not (
        0 <= next_row < grid_height and 
        0 <= next_col < grid_width
        ):
        continue

    next_square = lines[next_row][next_col]

    if next_square in pipes:
        if (-dir_row, -dir_col) in pipes[next_square]:
            current_pos = (next_row, next_col)
            prev_pos = (start_row, start_col)
            break


while current_pos != (start_row, start_col):
    path.add(current_pos)

    current_row, current_col = current_pos
    pipe = lines[current_row][current_col]
    exit1, exit2 = pipes[pipe]

    exit1_row, exit1_col = exit1
    exit2_row, exit2_col = exit2

    exit1_pos = (current_row + exit1_row, current_col + exit1_col)
    exit2_pos = (current_row + exit2_row, current_col + exit2_col)

    next_pos = (exit1_pos, exit2_pos)[exit1_pos == prev_pos]

    prev_pos = current_pos
    current_pos = next_pos


enclosed = 0

for row_num in range(grid_height):
    for col_num in range(grid_width):
        if (row_num, col_num) in path:
            continue 

        crossings = 0

        for c in range(col_num):
            if (row_num, c) in path:
                pipe_char = lines[row_num][c]
                if pipe_char in "|LJ":
                    crossings += 1
        
        if crossings % 2:
            enclosed += 1


print(enclosed)
