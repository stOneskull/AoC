with open("input.txt", "r") as file:
    steps = file.read().strip()

floor = 0

for pos, step in enumerate(steps, start=1):
    if step == "(":
        floor += 1
    elif step == ")":
        floor -= 1
        if floor == -1:
            break

print(pos)
