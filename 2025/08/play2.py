from itertools import combinations


with open("input.txt", "r") as file:
    boxes = [
        tuple(map(int, line.strip().split(","))) 
        for line in file
        ]


parent = {box: box for box in boxes}


def distance(p1, p2):
    """Calculates the squared Euclidean distance, avoiding a costly sqrt."""
    return (
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
        return True


pairs = sorted(
    combinations(boxes, 2), 
    key=lambda pair: distance(pair[0], pair[1])
    )

circuits = len(boxes)

for box1, box2 in pairs:
    if union(box1, box2):
        circuits -= 1
        if circuits == 1:
            break

print(box1[0] * box2[0])
