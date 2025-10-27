with open("input.txt", "r") as file:
    words = file.read().split()
    #print(len(words))

results = []

for word in words:
    result = ''
    for c in word:
        if c.isdigit():
            result += c
            break
    for c in word[::-1]:
        if c.isdigit():
            result += c
            break
    results.append(int(result))

print(sum(results))