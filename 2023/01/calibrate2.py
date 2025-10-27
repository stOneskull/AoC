with open("input.txt", "r") as file:
    lines = file.readlines()

digits = ['BLANK', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_digits(line):
    results = {}

    for d in digits[1:]:
        start_index = 0
        while True:
            try:
                index = line.index(d, start_index)
                results[index] = d
                start_index = index + 1
            except ValueError:
                break

    for i, c in enumerate(line):
        if c.isdigit():
            results[i] = c

    return results

results = []

for line in lines:
    word_digits = find_digits(line.strip())

    digit1 = word_digits[min(word_digits.keys())]
    if digit1 in digits:
        digit1 = str(digits.index(digit1))
    digit2 = word_digits[max(word_digits.keys())]
    if digit2 in digits:
        digit2 = str(digits.index(digit2))
    results.append(int(digit1 + digit2))

print(sum(results))