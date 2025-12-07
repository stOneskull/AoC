with open("input.txt", "r") as file:
    moveslist = file.read().strip()

houses = {(0, 0): 2}

moves = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

movers = {'santa': (0, 0), 'robo': (0, 0)}


for turn, move in enumerate(moveslist):
    mover = ('santa', 'robo')[turn % 2]
    at = movers[mover]   
    go = moves[move]
    at = (at[0] + go[0], at[1] + go[1])
    houses[at] = houses.get(at, 0) + 1
    movers[mover] = at


print(len(houses))
print(movers)
