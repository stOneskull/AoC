#optimized, generative

with open("input.txt", "r") as file:
    lines = file.read()

lines = lines.split(',')

ranges = []

max_stop = 0

for eachrange in lines:
    start, stop = map(int, eachrange.split('-'))
    ranges.append((start, stop))
    if stop > max_stop:
        max_stop = stop

max_len = len(str(max_stop))

invalids = set()

for repeat_len in range(1, max_len//2 + 1):
    for n in range(10**(repeat_len-1), 10**repeat_len):
        repeat = str(n)
        for repeats in range(2, max_len//repeat_len + 1):
            num_str = repeat * repeats
            num = int(num_str)
            if num > max_stop:
                break
            invalids.add(num)

sorted_invalids = sorted(invalids)

final_invalids = set()

for start, stop in ranges:
    for num in sorted_invalids:
        if num > stop:
            break
        if num >= start:
            final_invalids.add(num)


print(sum(final_invalids))
