with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]    

maxes = []

for line in lines:
    pos = 0
    digit = 0
    digits = 12
    digitlist = []
    line_len = len(line)

    for i in range(digits):
        remaining = digits - i - 1
        end = line_len - remaining
        
        digit = max(line[pos:end])
        digit_i = line.index(digit, pos, end)
        
        digitlist.append(digit)
        pos = digit_i + 1

    maxes.append(int("".join(digitlist)))


print(sum(maxes))
