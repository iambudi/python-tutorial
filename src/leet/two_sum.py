from typing import Dict, List

"""
Two Sum Problem
sum of two int element in a list match to the target int.
return the indices of two integers (as tuple or list)
example target 20 from [2,7,12,18] is indices (0,3)
2 + 18 = 20
"""


input_list = [1, 2, 17, 12, 18]
target = int(20)

#  python 3.10 union replaced with pipe
def two_sum_range(nums: List[int], target: int) -> List[int] | None:
    checked: Dict[int, int] = {}
    for i in range(len(nums)):
        if target - nums[i] in checked:
            return [checked[target - nums[i]], i]
        checked[nums[i]] = i

    return None


def two_sum_enum(nums: List[int], target: int) -> List[int]:
    checked: Dict[int, int] = {}
    diff: int
    for i, num in enumerate(nums):
        if (diff := target - num) in checked:
            return [checked[diff], i]
        checked[num] = i  # value as dict key for easier retrieve on return

    return []


# The following does not work when one of item is half of its target
def two_sum_dir(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        if target - num in nums:
            return [i, nums.index(target - num)]
    return []


def two_sum_comprehension(nums: list[int], target: int):
    return [(i, nums.index(target - num)) for i, num in enumerate(nums) if target - num in nums][0]


print(two_sum_range(input_list, target))
print(two_sum_enum(input_list, target))
print(two_sum_dir(input_list, target))
print(two_sum_comprehension(input_list, target))

from itertools import combinations

# https://codereview.stackexchange.com/questions/212228/leetcode-two-sum-code-in-python/212232
def two_sum_combi(nums: List[int], target: int):
    # combinations yield n tuples as of second arg
    for (i, first), (j, second) in combinations(enumerate(nums), 2):
        if first + second == target:
            return [i, j]

    return None


print(two_sum_combi(input_list, target))
