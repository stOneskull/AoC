from math import sqrt
from itertools import combinations
from collections import Counter


with open("input.txt", "r") as file:
    boxes = [
        tuple(map(int, line.strip().split(","))) 
        for line in file
        ]


parent = {box: box for box in boxes}


def distance(p1, p2):
    return sqrt(
        (p1[0] - p2[0])**2 +
        (p1[1] - p2[1])**2 +
        (p1[2] - p2[2])**2
    )


def find_leader(box):
    if parent[box] == box:
        return box
    parent[box] = find_leader(parent[box])
    return parent[box]


def union(box1, box2):
    leader1 = find_leader(box1)
    leader2 = find_leader(box2)
    if leader1 != leader2:
        parent[leader2] = leader1


pairs = sorted(
    combinations(boxes, 2), 
    key=lambda pair: distance(pair[0], pair[1])
    )

for pair in pairs[:1000]:
    union(pair[0], pair[1])


leaders = [find_leader(box) for box in boxes]
sizes = Counter(leaders)
sorted_sizes = sorted(sizes.values(), reverse=True)
a, b, c = sorted_sizes[:3]

print(a * b * c)
