from typing import Dict

def df(nums, target):
    for i in nums:
        j = target - i
        start_index = nums.index(i)
        next_index = start_index + 1
        temp_nums = nums[next_index:]
        if j in temp_nums:
            return nums.index(i), next_index + temp_nums.index(j)


def kf(nums, target):

    dies = {}

    for i in range(len(nums)):
        if target - nums[i] not in dies:
            dies[nums[i]] = i
        else:
            return [dies[target - nums[i]], i]


class Solution:
    pass
