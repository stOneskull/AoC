with open("input.txt", "r") as file:
    lines = file.readlines()

max_len = max(len(line.strip()) for line in lines)

grid = [line.strip().ljust(max_len) for line in lines]


def solve(problem):
    operator = problem.pop().strip()

    cols = zip(*problem)
    
    terms = ["".join(col).strip() for col in cols]

    return eval(operator.join(terms))


total = 0
col_start = 0

for c in range(max_len):
    if all(line[c] == ' ' for line in grid):
        problem = [line[col_start:c] for line in grid]
        total += solve(problem)
        col_start = c + 1

last_problem = [line[col_start:] for line in grid]

total += solve(last_problem)


print(total)
