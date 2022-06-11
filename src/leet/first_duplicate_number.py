from typing import List
"""
Return value of duplicate number found in a list
with shortest occurrance index
Input: [2,1,3,5,3,2]
Output: 3 not 2. 2 has longer index distance between two occurances compared to 3
Return -1 if not found
"""

def first_duplicate(numbers: List[int]) -> int:
    """
    Put each number in a list and find if there's occurance
    This is more eficient. Auto distance check!
    2 come first but no occurance till end of list
    while double 3 exists in between so return 3.
    """
    dups: List[int] = list()
    for num in numbers:
        if num in dups:
            return num
        dups.append(num)
    return -1


input = [4, 2, 1, 3, 5, 3, 2]
print("First duplicate set should be 3 =>", first_duplicate(input))


def first_duplicate_zip(numbers: List[int]) -> int:
    # remove non duplicate using count, remains the dups [2,3,3,2]
    # find consecutive number to get shortest distance
    dups = [num for num in numbers if numbers.count(num) > 1]
    # can use groupby as alternative of zip
    for curr, next in zip(dups, dups[1:]): # compare with next number
        if curr == next:
            return curr # 3,3 is first duplicate
    return -1

input = [4, 1, 2, 3, 5, 3, 2]
print("First duplicate should be 3 =>", first_duplicate_zip(input))

input = [1,2,3]  # not found
print("Not found should be -1 =>", first_duplicate_zip(input))