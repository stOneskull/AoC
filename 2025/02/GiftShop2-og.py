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
        #if num < 11:
            #continue
        num_str = str(num)
        num_len = len(num_str)

        for repeat_len in range(1, num_len//2 + 1):
            if num_len % repeat_len == 0:
                repeat = num_str[:repeat_len]
                repeats = num_len//repeat_len
                if repeat * repeats == num_str:
                    invalids.add(num)
                    break 

print(sum(invalids))