from itertools import combinations
from multiprocessing import Pool

from shapely.geometry import Polygon, box


with open("input.txt", "r") as file:
    red_tiles = [
        tuple(map(int, line.strip().split(","))) 
        for line in file
        ]


theater_floor = Polygon(red_tiles)


def check_rectangle(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    
    candidate_rectangle = box(
        min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        )

    if theater_floor.contains(candidate_rectangle):
        return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    return 0


with Pool() as pool:
    areas = pool.starmap(
        check_rectangle, combinations(red_tiles, 2)
        )

print(max(areas))
