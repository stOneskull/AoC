with open("input.txt", "r") as file:
    lines = file.readlines()

rows = [line.strip() for line in lines]
rows_copy = rows.copy()


grid_height = len(rows)
grid_width = len(rows[0])

#print(grid_height, grid_width)

for i, row in enumerate(rows_copy):
    if '#' not in row:
        rows[i] = '2' * grid_width

for i in range(grid_width):
    if not any(row[i] == '#' for row in rows_copy):
        for row in rows:
            #row[i] = '2'
            ...
test = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
""".strip().splitlines()

print(test)