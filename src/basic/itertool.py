"""
The itertools module is a collection of tools intended to be fast
and use memory efficiently when handling iterators
All itertool methods return iteration
"""
from itertools import accumulate, takewhile, dropwhile, count
import operator
from typing import List

def generate_multiply(max: int) -> list[int]:
    numbers: List[int] = []
    # pylance does not recognize num type
    for num in count(start=1, step=2):
        numbers.append(num * num)
        if num > max:
            break

    return numbers


numbers = generate_multiply(10)
print("Generated", numbers)

# Accumulate (sum). This still return a new list not a single value like reduce
print("Accumulate", list(accumulate(numbers, operator.add, initial=0)))

filters = takewhile(lambda x: x < 10, numbers)
print("Takewhile < 10", list(filters))

# dropwhile is not like filter()
# it drop elements as long the predicate is true;
# afterward return every element
# since first numbers true but 7 is falsy for n % 2 so
# it drop only 4 and return the rest [7 to 17]
numbers = [4, 7, 11, 2, 13, 17]
print("Filter", list(filter(lambda n: n % 2 == 0, numbers)))
print("Dropwhile", list(dropwhile(lambda n: n % 2 == 0, numbers)))

li = [2, 4, 5, 7, 8]
# using dropwhile() to start displaying after condition is false
print("The values after condition returns false : ", end="")
print(list(dropwhile(lambda x: x % 2 == 0, li)))

# there's another itertools methods like product, perm etc
# see the doc
