with open("input.txt", "r") as file:
    boxes = file.read().splitlines()


ribbon = 0

for box in boxes:
    dimensions = [*map(int, box.split("x"))]
    l, w, h = dimensions
    perimeter = min(l+w, w+h, h+l) * 2
    volume = l * w * h
    ribbon += perimeter + volume


print(ribbon)
