with open("input.txt", "r") as file:
    lines = file.read().split('\n\n')

lines.pop() 
fresh_ranges = lines.pop().splitlines()
fresh_ranges = [list(map(int, r.split('-'))) for r in fresh_ranges]
fresh_ranges.sort()

merged_ranges = [fresh_ranges[0]]


for start, end in fresh_ranges[1:]:
    last_start, last_end = merged_ranges[-1]

    if start <= last_end+1:
        merged_ranges[-1][1] = max(end, last_end)
    else:
        merged_ranges.append([start, end])


total = sum(end-start+1 for start, end in merged_ranges)

print(total)
