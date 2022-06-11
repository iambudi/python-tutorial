"""
Find first unique char in a string (non repeating char) 
example: aaabdeddeaffc
output: index 3 (which is b)
return -1 if not found
"""
from collections import Counter


def first_unique_char_index(input: str) -> int:
    for idx, chr in enumerate(input):
        # if cur idx equals last index of chr means unique char in the string
        if idx == input[idx:].rindex(chr):
            return idx
    return -1


# One liner lover
def first_unique_char_dict(input: str) -> int:
    # [] or [-1] will give [-1], so take only first idx
    # NOTE: set() is not guaranteed in order, so can give wrong result
    # To keep the order use dict.fromkeys(input) => {'a': None, 'b': None so on}
    # dataset : Dict[str, int] = {}
    # for x in range(len(input)):
    #     dataset[input[x]] = dataset.get(x, 0) + 1

    my_dict = [input.index(chr) for chr in set(input) if input.count(chr) == 1] or [-1]
    return my_dict[0]


def first_unique_char_counter(input: str) -> int:
    # Counter = a:3, b:2 so on
    return ([input.index(k) for k, v in Counter(input).items() if v == 1] or [-1])[0]
    # return my_dict[0]
    # for k, v in Counter(input).items():
    #     if v == 1:
    #         return input.index(k)
    # return -1


input = "aaabdbddeaffcc"
print("Unique by index at", first_unique_char_index(input))
print("Unique by dict at", first_unique_char_dict(input))
print("Unique by counter at", first_unique_char_counter(input))
