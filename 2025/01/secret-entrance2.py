with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.split() for line in lines]

rotations = [(rot[0], int(rot[1:])) for line in lines for rot in line]

turns = 0

dial = 50

for rot in rotations:
    clicks, rotation = divmod(rot[1], 100)
    turns += clicks

    if rot[0] == "R":
        if dial + rotation >= 100:
            turns += 1
        dial = (dial + rotation) % 100
    else: #rot[0] == "L":
        if dial and dial - rotation <= 0:
            turns += 1
        dial = (dial - rotation) % 100

print(turns)
