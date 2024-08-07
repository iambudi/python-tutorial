from array import array
from typing import List, NamedTuple, Set

"""
Python non primitive data structure
"""
"""
IMMUTABLE
1. Tuple & Named Tuple
=========================================================================================
"""

my_tuple = (1, 2, 3)
# Named Tuple untyped
Student = NamedTuple("Student", [("id", int), ("name", str)])

# 2. Named Tuple with type hint.
# Second arg as list of tuple name, type
User = NamedTuple("User", [("id", int), ("name", str)])
user = User(1, "admin")
print("Named Tuple", f"{user.name} has id {user[0]}")

"""
MUTABLE
1. List (Array)
=========================================================================================
"""
numbers: List[int] = [1, 3, 4, 5, 6, 7]

# Slicing by element index [start:stop:step]
print("Slice all numbers", numbers[:])  # exclude first element
print("Slice by two steps", numbers[0:5:2])  # start from index 0 till 5 => [1,4,6]
print("Slice exclude last two", numbers[:-2])
print("Slice first two", numbers[:2])
print("Slice from second el", numbers[2:])  # from index 2 to end of list
print("Slice with same index:index return nothing", numbers[2:2])

# Add and remove element
numbers.append(10)
numbers.pop()  # pop last element in the list
numbers.pop(0)  # pop by element index
print("Number after pop should not contain 1", numbers)
print("Index of value 5 is", numbers.index(5))

# different ways to clear list
numbers.clear()
numbers = []  # reinitialize
numbers *= 0  # not well known
del numbers[:]  # del range start to end
print("Numbers after clear", numbers)

"""
2. Set: unordered, no duplicate (unique collection)
=========================================================================================
"""
# 2 ways to init set
mySet: Set[int] = set()
mySet = set[int]()  # use () to differentiate with generic type alias
# mySet = {} <-- this does not work, it's not dict
print("Empty set", type(mySet))

mySet = {1, 2, 2, 3, 3, 3}
mySet = set([1, 2, 3, 4, 5, 5, 5, 5, 5])

mySet.add(100)
mySet.add(200)
print("Set unique:", mySet)

for i, s in enumerate(mySet):
    print(f"Set {i}. {s}")

"""
3. Dictionary
=========================================================================================
"""
userDict = {"id": 1, "name": "Admin"}
# Missing key no error raise with default value
print("Dict has key age? ", userDict.get("age", None))
mergeDict = userDict | {"age": 10, "sex": "male"}
print("Merge Dict", mergeDict)

# items means {k:v}, values only v and keys only k
for key, val in userDict.items():
    print("Dict Iterator Key Val: {%s: %s}" % (key, val))


def register(users: list[User]):
    """
    collection can be used as typehint.
    here we use `User` as a named tuple
    """
    for usr in users:
        print(f"Register user {usr.name} success")


user1 = User(1, "Monthy")
user2 = User(1, "Python")
register([user1, user2])

"""
# 4. Array
=========================================================================================
Python does not have array as primitive data structure in the same sense as lists or tuples
It's provided by the array module. In term of functionality similar to list.
+ compact and storage efficient (store their elements in a contiguous block of memory)
+ functionality: behave very much like lists
+ performance: faster for for numeric operations for large dataset
- objects stored is constrained in single type (not heterogeneous)
========================================================================================
typecode: i = signed int, I unsigned, f float, d double, b = char
complete list of typecode
refer https://docs.python.org/3/library/array.html
========================================================================================
"""
# first arg is typecode
ary_int = array("i", [1, 2, 3, 4])  # this would be invalid [1,2,3,"4"])
print("Type of ary is", type(ary_int))
# another typecode
print(ary_int, array("u", "hello \u2641"), array("d", [1.0, 2.0]))
