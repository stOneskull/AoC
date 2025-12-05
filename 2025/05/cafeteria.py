with open("input.txt", "r") as file:
    lines = file.read().split('\n\n')

available = map(int, lines.pop().splitlines())
fresh_ranges = lines.pop().splitlines()
fresh_ranges = [list(map(int, r.split('-'))) for r in fresh_ranges]

fresh = 0

for item in available:
    if any(start <= item <= end for start, end in fresh_ranges):
        fresh += 1

print(fresh)
