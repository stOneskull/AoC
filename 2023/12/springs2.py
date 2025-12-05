from functools import cache


with open("input.txt", "r") as file:
    lines = file.readlines()

guides = []

for line in lines:
    guide, nums_str = line.strip().split()
    nums = tuple(map(int, nums_str.split(',')))
    guides.append((guide, nums))


def arrange(guide, nums):

    @cache
    def arranger(i, num_i, batch_len):
        if i == len(guide):
            if batch_len == 0 and num_i == len(nums):
                return 1
            if num_i == len(nums)-1 and batch_len == nums[num_i]:
                return 1
            return 0

        guide_total = 0
        char = guide[i]

        if char in '.?':
            if batch_len == 0:
                guide_total += arranger(i+1, num_i, 0)
            elif num_i < len(nums) and batch_len == nums[num_i]:
                guide_total += arranger(i+1, num_i+1, 0)

        if char in '#?':
            guide_total += arranger(i+1, num_i, batch_len+1)

        return guide_total


    return arranger(0, 0, 0)


arrangements = 0

for guide, nums in guides:
    newguide = '?'.join([guide] * 5)
    newnums = nums * 5

    arrangements += arrange(newguide, newnums)

print(arrangements)
