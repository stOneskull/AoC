with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

#print(len(lines), len(lines[0])) == 140 x 140

length = len(lines)

#copy of part1 to edit later, my brain is cooked..

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

for dir_row, dir_col in (n, s, w, e):
    next_row = start_row + dir_row
    next_col = start_col + dir_col
    
    if not (
        0 <= next_row < length and 
        0 <= next_col < length
        ):
        continue

    next_square = lines[next_row][next_col]

    if next_square in pipes:
        if (-dir_row, -dir_col) in pipes[next_square]:
            current_pos = (next_row, next_col)
            prev_pos = (start_row, start_col)
            steps = 1
            break


while current_pos != (start_row, start_col):
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
    steps += 1
 
print(steps // 2)
