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

parts = []

for (row, col), part in numbers.items():
    is_part = False
    
    for i in range(len(part)):
        digit_row = row
        digit_col = col + i

        for drow in [-1, 0, 1]:
            for dcol in [-1, 0, 1]:
                if drow == dcol == 0:
                    continue

                neighbor_row = digit_row + drow
                neighbor_col = digit_col + dcol

                neighbor_char = charmap.get((neighbor_row, neighbor_col))

                if neighbor_char and neighbor_char != '.' and not neighbor_char.isdigit():
                    is_part = True
                    break 
            if is_part:
                break 
        if is_part:
            break 

    if is_part:
        parts.append(int(part))

#print(parts)
print(sum(parts))
