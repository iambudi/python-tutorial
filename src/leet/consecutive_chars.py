from typing import Dict, List
from itertools import groupby
from itertools import zip_longest

"""
=========================================================================================
Count consecutive repeated chars from a string and return in a List of Dictionary
Input   : 'aaaabbbccca' (note a at the end of string)
Output  : [{'a': 4}, {'b': 3}, {'c': 2}, {'a': 1}]
=========================================================================================
"""

Output = List[Dict[str, int]]


def count_consecutive_chars(input: str) -> Output:
    output: Output = []
    temp_list: List[str] = []
    for i, chr in enumerate(input):  # index must use enumerate
        temp_list.append(chr)
        # prevent index out of range
        if i + 1 < len(input) and chr == input[i + 1]:
            continue
        output.append({chr: len(temp_list)})
        temp_list.clear()
    return output


# zip() has problem since 'a' at the end of string does not have pair for next
# so it's ignoring it. To make it paired use zip_longest which perfectly pair with None
def count_consecutive_zip(input: str) -> Output:
    output: Output = []
    temp_list: List[str] = []
    for cur, next in zip_longest(input, input[1:]):  # (a, a), (a, b) so on
        temp_list.append(cur)
        print(cur, ":", next)
        if cur == next:  # (a == None) means end of loop
            continue

        output.append({cur: len(temp_list)})
        temp_list.clear()
    return output


def count_consecutive_simple(input: str) -> Output:
    output: Output = []
    temp_list: List[str] = []
    for chr in input:
        if chr in temp_list or not temp_list:  # append to temp if empty or same char
            temp_list.append(chr)
            continue
        output.append({temp_list[0]: len(temp_list)})
        temp_list = [chr]  # clear and add
    return output + [{temp_list[0]: len(temp_list)}]


# One liner using itertools
def count_consecutive_group(input: str) -> Output:
    # group chars to a,b,c,a
    # Note: iterator can't be counted until it's finished iterating
    # create comprehension from group items each char a => a,a,a,a.
    # for each chr item set as 1 and sum it
    # return [{chr: sum(1 for _ in group)} for chr, group in groupby(list(input))]
    # other than comprehension, convert to list and count its len
    return [{chr: len(list(group))} for chr, group in groupby(list(input))]


print(count_consecutive_zip("aaaabbbcca"))
print(count_consecutive_simple("aaaabbbcca"))
print(count_consecutive_group("aaaabbbcca"))
