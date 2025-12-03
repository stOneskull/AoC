with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]    

maxes = []

for line in lines:
    max_num = 0
    first = '0'

    for c in line:
        num = int(first + c)
        max_num = max(max_num, num)
        first = max(first, c)

    maxes.append(max_num)


print(sum(maxes))
