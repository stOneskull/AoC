with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

total = 0

for line in lines:
    winners, mynums = line.split(":")[1].split("|")

    winners = set(winners.split())
    mynums = set(mynums.split())

    if not (intersection := winners & mynums):
        continue

    total += 2**(len(intersection) - 1)

print(total)
