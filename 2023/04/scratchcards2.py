with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]


games = {}

for game, line in enumerate(lines, start=1):
    winners, mynums = line.split(":")[1].split("|")

    winners = set(winners.split())
    mynums = set(mynums.split())

    games[game] = len(winners & mynums)

#print(games)

memo = {}

def scratch(card):
    if card in memo:
        return memo[card]

    total = 1
    for nextcard in range(1, games.get(card, 0) + 1):
        total += scratch(card + nextcard)

    memo[card] = total
    return total


cards = sum(scratch(card) for card in games)

print(cards)
