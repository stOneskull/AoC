from itertools import combinations


with open("input.txt", "r") as file:
    tiles = {
        tuple(map(int, line.strip().split(",")))
        for line in file
    }


max_area = 0

for (x1, y1), (x2, y2) in combinations(tiles, 2):
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

    if area > max_area:
        max_area = area


print(max_area)
