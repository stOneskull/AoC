from collections import Counter


with open("input.txt", "r") as file:
    lines = file.read().splitlines()

S_index = lines[0].find("S")

timelines = Counter({S_index: 1})


for row in lines[1:]:
    next_timelines = Counter()

    for c, count in timelines.items():
        if row[c] == '^':
            next_timelines[c-1] += count
            next_timelines[c+1] += count
        else:
            next_timelines[c] += count
    
    timelines = next_timelines


total_timelines = sum(timelines.values())

print(total_timelines)
