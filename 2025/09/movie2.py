from itertools import combinations

from shapely.geometry import Polygon, box


with open("input.txt", "r") as file:
    red_tiles = [tuple(map(int, line.strip().split(","))) for line in file]


max_area = 0

valid_area_polygon = Polygon(red_tiles)

red_tiles_set = set(red_tiles)


for p1, p2 in combinations(red_tiles_set, 2):
    x1, y1 = p1
    x2, y2 = p2

    candidate_rectangle = box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))

    if valid_area_polygon.contains(candidate_rectangle):
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        max_area = max(max_area, area)

print(max_area)
