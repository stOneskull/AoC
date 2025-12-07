with open("input.txt", "r") as file:
    lines = file.read().splitlines()

S_index = lines[0].find("S")


beams = {S_index}
splits = 0


for row in lines[1:]:
    next_beams = set()

    for c in beams:
        if row[c] == '^':
            next_beams.add(c-1)
            next_beams.add(c+1)
            splits += 1
        else:
            next_beams.add(c)
    
    beams = next_beams


print(splits)
