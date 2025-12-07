with open("input.txt", "r") as file:
    moveslist = file.read().strip()

houses = {(0, 0): 1}
moves = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}

at = (0, 0)

for move in moveslist:
    go = moves[move]
    at = (at[0] + go[0], at[1] + go[1])
    houses[at] = houses.get(at, 0) + 1


print(len(houses))
