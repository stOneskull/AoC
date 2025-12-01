with open("input.txt", "r") as file:
    lines = file.readlines()


def solve(line):
    lines = [line]

    while any(line):
        line = [line[i] - line[i-1] for i in range(1, len(line))]
        lines.append(line)

    answer = sum(line[-1] for line in lines)
 
    return answer
    

lines = [line.strip() for line in lines]

answers = []

for line in lines:
    line = [int(value) for value in line.split()]
    answers.append(solve(line))

#print(answers)
print(sum(answers))