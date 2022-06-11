"""
=========================================================================================
list comprehension is syntatic construct for creating a list based on existing lists. 
It can be applied to tuple, set and dictionary
=========================================================================================
# tuple is not faster than list. Both in comprehension or generator expression
# python3 -m timeit "a = [i for i in range(1000)]"      <-- list is faster
# python3 -m timeit "a = tuple(i for i in range(1000))" <-- tuple is slower here
# python3 -m timeit "a = tuple(range(1000))"            <-- tuple is still slower
# python3 -m timeit "a = list(range(1000))"
=========================================================================================
"""
from typing import List

numbers = [1, 2, 3, 4]
# 1. List Comprehension
list_numbers: List[int] = [i - 1 for i in numbers]  # new list in just one line
print("List:", list_numbers)

# Compare with 3 lines below
list_numbers = []
for i in numbers:
    list_numbers.append(i - 1)

# 2. Set comprehension
fruits = {"orange", "apple", "banana"}
set_fruits = {s.upper() for s in fruits}  # {"ORANGE","APPLE", "BANANA"}
print("Set:", set_fruits)

# 3. Dict comprehension
fruits = {1: "orange", 2: "apple", 3: "banana"}
dict_fruits = {
    v: k for k, v in fruits.items()
}  # {"orange": 1, "apple", 2, "banana": 3}
# can apply string method as well:
dict_fruits = {v.upper(): k for k, v in fruits.items()}
print("Dict:", dict_fruits)

# 4. Mix Generation f.e from dict to list
lang = {"name": "python", "age": 10}
# Construct list of string using interpolation
list_lang = ["{}:{}".format(k.upper(), v) for k, v in lang.items()]
# ['NAME:python', 'AGE:10']
print("List:", list_lang)
