with open("input.txt", "r") as file:
    text = file.read()

blocks = text.strip().split('\n\n')

seed_line = blocks[0].split(':')[1].strip().split()

seeds = list(map(int, seed_line))

def parse_map(block):
    lines = block.split('\n')[1:]
    map_ranges = []
    for line in lines:
        dest_start, src_start, range_len = map(int, line.split())
        map_ranges.append((dest_start, src_start, range_len))
    return map_ranges

maps = [parse_map(block) for block in blocks[1:]]

locations = []
for seed in seeds:
    current_number = seed

    for x_map in maps:
        
        for dest_start, src_start, range_len in x_map:
            if src_start <= current_number < src_start + range_len:
                current_number = dest_start + (current_number - src_start)
                break

    locations.append(current_number)

print(min(locations))
