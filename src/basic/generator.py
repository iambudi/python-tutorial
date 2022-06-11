"""
=========================================================================================
generator are a special kind of function that return a lazy iterator object
that can be looped over like a list. However, unlike lists, lazy iterators do not store 
their contents in memory.
Example cases: 
a. Create infinite or large sequence numbers    [1 - n]
b. Reading huge text file                       [csv in hundreds MB size]
Putting all the sequnece of numbers or whole lines of file as a list
could take some times and consume a lot of memory, it would be more efficient to 
proceed it one number or line at a time by using generator.
=========================================================================================
There are two kinds of generators
1. Generator Function   : generate using yield keyword
2. Generator Expression : generate inside list comprehension
=========================================================================================
"""
# 1. Generator Function
def my_generator():
    n = 1
    print(f"Yielding first {n}")
    # yield will remember the state
    # and continue upon next() generation call
    yield n  # pauses and returns value to the caller

    # continue call
    n = 2
    print(f"Yielding second {n}")
    yield n


# Here my_generator does not return all numbers [1,2] at once
# But return the element one by one as the iteration
for n in my_generator():
    print("Iterator receive:", n)

print(list(my_generator()))

# use next if we need to controll getting the data from generator
gen = my_generator()
print("First value", next(gen))
print("Second with next", next(gen))

# Python has 3 methods to read file line
# refer https://www.stechies.com/read-file-line-by-line-python/#4
# carefull not to manually split using f.read().split("\n") since it read all the content first
def file_reader(file_name: str):
    # here read using context manager
    with open(file_name, "r") as f:
        for line in f:
            yield line.strip()


# read current python file
for line in file_reader(__file__):
    print(line)

# 2. Generator expression
# bracket () is identifier for generator not tuple
# that's why for tuple comprehension should use tuple() keyword
gen_numbers = (n for n in range(10))
list_numbers = [n for n in range(10)]  # real list []
print("gen_numbers type is ", type(gen_numbers))  # <class 'generator'>
print("list_numbers type is ", type(list_numbers))  # <class 'list'>

# since gen_numbers is generator so it needs to convert to list to print
print("gen_numbers", list(gen_numbers))
