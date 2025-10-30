with open("input.txt", "r") as file:
    text = file.read()

blocks = text.strip().split('\n\n')

seed_line = blocks[0].split(':')[1].strip().split()

seed_pairs = list(map(int, seed_line))

current_ranges = []

for i in range(0, len(seed_pairs), 2):
    current_ranges.append(
        (seed_pairs[i], seed_pairs[i] + seed_pairs[i+1])
        )


def parse_map(block):
    lines = block.split('\n')[1:]
    map_ranges = []

    for line in lines:
        if not line:
            continue
        dest_start, src_start, range_len = map(int, line.split())
        map_ranges.append((dest_start, src_start, range_len))

    return map_ranges


maps = [parse_map(block) for block in blocks[1:]]

for x_map in maps:
    new_ranges = []

    while current_ranges:
        start, end = current_ranges.pop()

        found_overlap = False

        for dest_start, src_start, range_len in x_map:
            src_end = src_start + range_len
            overlap_start = max(start, src_start)
            overlap_end = min(end, src_end)

            if overlap_start < overlap_end:
                new_ranges.append(
                    (dest_start + (overlap_start - src_start), 
                     dest_start + (overlap_end - src_start))
                     )
                
                if start < overlap_start:
                    current_ranges.append((start, overlap_start))

                if overlap_end < end:
                    current_ranges.append((overlap_end, end))
                    
                found_overlap = True
                break
        
        if not found_overlap:
            new_ranges.append((start, end))
    
    current_ranges = new_ranges

#print(current_ranges)
print(min(loc_range[0] for loc_range in current_ranges))
