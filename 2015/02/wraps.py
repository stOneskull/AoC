with open("input.txt", "r") as file:
    boxes = file.read().splitlines()


paper = 0

for box in boxes:
    dimensions = [*map(int, box.split("x"))]
    l, w, h = dimensions
    sides = [l*w, w*h, h*l]
    paper += sum(sides) * 2 + min(sides)

print(paper)
