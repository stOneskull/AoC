# with open("input.txt", "r") as file:
#     lines = file.read()

# lines = lines.split(',')

invalids = set()

start = 11
stop = 4294942950

max_len = 10


for repeat_len in range(1, max_len//2 + 1):
    for n in range(10**(repeat_len-1), 10**repeat_len):
        repeat = str(n)
        for repeats in range(2, max_len//repeat_len + 1):
            num_str = repeat * repeats
            num = int(num_str)
            if num >= stop:
                break

            invalids.add(num)


print(sum(invalids))
