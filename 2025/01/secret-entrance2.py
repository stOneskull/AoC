with open("input.txt", "r") as file:
    lines = file.readlines()

rotations = [(rote[0], int(rote[1:])) for rote in lines]

zeros = 0
dial = 50

for rote in rotations:
    clicks, rotation = divmod(rote[1], 100)
    zeros += clicks

    if rote[0] == "R":
        if dial + rotation >= 100:
            zeros += 1
        dial = (dial + rotation) % 100
    else:
        if dial and dial - rotation <= 0:
            zeros += 1
        dial = (dial - rotation) % 100

print(zeros)
