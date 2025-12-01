with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.split() for line in lines]

rotations = [(rot[0], int(rot[1:])) for line in lines for rot in line]

turns = 0

dial = 50

for rot in rotations:
    if rot[0] == "R":
        dial = (dial + rot[1]) % 100
    elif rot[0] == "L":
        dial = (dial - rot[1]) % 100

    if dial == 0:
        turns += 1

print(turns)