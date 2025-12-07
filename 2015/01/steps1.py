with open("input.txt", "r") as file:
    steps = file.read().strip()

floor = 0

for step in steps:
    if step == "(":
        floor += 1
    elif step == ")":
        floor -= 1

print(floor)