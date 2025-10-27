with open("input.txt", "r") as file:
    lines = file.readlines()

def powersum(cubes):
    power = 1
    for color in ['red', 'green', 'blue']:
        power *= cubes[color]
    return power


powers = []

for line in lines:

    game, hands = line.split(':')
    game_id = int(game.split(' ')[1])

    cubes = {'red': 0, 'green': 0, 'blue': 0}

    for hand in hands.strip().split(';'):
        for n_cubes in hand.strip().split(','):
            count, color = n_cubes.strip().split(' ')
            cubes[color] = max(cubes[color], int(count))
            
    powers.append(powersum(cubes))

print(sum(powers))