with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip().split() for line in lines]

total = 0

for c in range(len(lines[0])):
    #print(c)
    problem = []
    for line in lines:
        problem.append(line[c])
    print(problem)

    operator = problem[-1]

    problem = operator.join(problem[:-1])

    print(problem)
    print(eval(problem))
    
    total += eval(problem)

print(total)
