from math import lcm


with open("input.txt", "r") as file:
    lines = file.read()

directions = lines.split('\n\n').pop(0).strip()

lines = lines.splitlines()[2:]

network = {}

for line in lines:
    at, go = line.split(' = ')
    l, r = go.strip('()').split(', ')
    network[at] = (l, r)

lr_dict = {'L': 0, 'R': 1}


def bounce(pos, steps):
    for direction in directions:
        move = lr_dict[direction]

        pos = network[pos][move]

        steps += 1

        if pos.endswith('Z'):
            return steps, pos
        
    return steps, pos


starters = [at for at in network if at.endswith('A')]

runs = []

for starter in starters:
    pos = starter
    steps = 0
    while not pos.endswith('Z'):
        steps, pos = bounce(pos, steps)
    runs.append(steps)

result = lcm(*runs)

print(result)
