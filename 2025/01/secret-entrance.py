with open("input.txt", "r") as file:
    lines = file.readlines()

rotations = [(rote[0], int(rote[1:])) for rote in lines]

zeros = 0
dial = 50

for rote in rotations:
    if rote[0] == "R":
        dial = (dial + rote[1]) % 100
    else:
        dial = (dial - rote[1]) % 100

    if dial == 0:
        zeros += 1

print(zeros)
