from itertools import zip_longest

"""
An iterator is an object that contains a countable number of values that can be iterated upon, 
meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().
"""

actors = ["Keanu Reeves", "Dwyne Johnson", "Tom Holland", "Iko Uwais", "Robert Downey Jr."]
movies = ("John Wick", "Skyscraper", "Spiderman", "The Raid")

"""
The zip() function returns a zip object, which is an iterator of tuples 
where the first item in each passed iterator is paired together, and then 
the second item in each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with 
the least items decides the length of the new iterator.
"""
print("zip", list(zip(actors, movies)))  # Here we miss the Robert pair since movies only have 4 items
actors.append("Ben Affleck")  # make actors len different so no pairing with movie
print("zip in balance, will skip ben affleck", list(zip(actors, movies)))  # Here we miss Ben pair since movies only have 4 items

# zip longest will show ben affleck but with pairing of None. It takes the longest iterable
print("zip longest", list(zip_longest(actors, movies)))

print("max", max([1, 2, 3, 4, 5]))
