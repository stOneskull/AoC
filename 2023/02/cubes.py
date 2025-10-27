with open("input.txt", "r") as file:
    lines = file.readlines()

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

possibles = []

for line in lines:

    game, hands = line.split(':')
    game_id = int(game.split(' ')[1])

    possible = True

    for hand in hands.strip().split(';'):
        for n_cubes in hand.strip().split(','):
            count, color = n_cubes.strip().split(' ')
            if int(count) > bag[color]:
                possible = False
                break 
        if not possible:
            break 

    if possible:
        possibles.append(game_id)

print(sum(possibles))