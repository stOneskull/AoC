with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

charmap = {}

for row_num, row in enumerate(lines):
    for col_num, char in enumerate(row):
        charmap[(row_num, col_num)] = char

numbers = {}

for row_num, row in enumerate(lines):
    number = ""
    for col_num, char in enumerate(row):
        if char.isdigit():
            if number == "":
                number_start = col_num
            number += char
        elif number:
            numbers[(row_num, number_start)] = number
            number = ""
    if number:
        numbers[(row_num, number_start)] = number


from collections import defaultdict

gears = defaultdict(list)

for (row, col), num in numbers.items():
    found_gears = set()
    
    for i in range(len(num)):
        digit_row = row
        digit_col = col + i

        for drow in [-1, 0, 1]:
            for dcol in [-1, 0, 1]:
                if drow == 0 and dcol == 0:
                    continue

                neighbor_row = digit_row + drow
                neighbor_col = digit_col + dcol
                neighbor_pos = (neighbor_row, neighbor_col)

                if charmap.get(neighbor_pos) == '*' and neighbor_pos not in found_gears:
                    gears[neighbor_pos].append(int(num))
                    found_gears.add(neighbor_pos)

total = 0
for gear_pos, neighbors in gears.items():
    if len(neighbors) == 2:
        total += neighbors[0] * neighbors[1]

print(total)
