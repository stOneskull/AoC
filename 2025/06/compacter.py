with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip().split() for line in lines]

total = 0

for c in range(len(lines[0])):
    problem = []
    for line in lines:
        problem.append(line[c])

    operator = problem.pop()

    problem = operator.join(problem)
    
    total += eval(problem)

print(total)
