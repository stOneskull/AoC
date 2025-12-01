with open("input.txt", "r") as file:
    lines = file.readlines()


def solve(line):
    lines = [line]

    while any(line):
        line = [line[i] - line[i-1] for i in range(1, len(line))]
        lines.append(line)
    
    answer = 0

    for line in lines[::-1]:
        answer = line[0] - answer
    
    return answer
    

lines = [line.strip() for line in lines]

answers = []

for line in lines:
    line = [int(value) for value in line.split()]
    answers.append(solve(line))

print(sum(answers))
