#iterative, brute-force

with open("input.txt", "r") as file:
    lines = file.read()

lines = lines.split(',')

invalids = set()

for eachrange in lines:
    start, stop = eachrange.split('-')
    start = int(start)
    stop = int(stop)
    
    for num in range(start, stop+1):
        num_str = str(num)
        if (num_len := len(num_str)) % 2:
            continue
        if num_str[:num_len // 2] == num_str[num_len // 2:]:
            invalids.add(num)

print(sum(invalids))