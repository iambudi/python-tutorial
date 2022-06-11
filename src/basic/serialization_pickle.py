from datetime import datetime
import os
import pickle
from typing import Any, Dict, List
import bz2

"""
=========================================================================================
Pickle (also called marshalling or flattening) is used for serializing and de-serializing
Python object structures. 
NOTE: Pickle is not a compression tool, but pickle can store data with compression algo
such as bzip2, gzip etc
=========================================================================================
Pickle is very useful when working with ML algorithms, where we want to save them 
and be able to make new predictions at a later time, without having to rewrite everything
or train the model all over again.
=========================================================================================
Caveats:
1. Its protocol is specific to Python. Cross-language compatibility is not guaranteed.
2. Unpickling a file that was pickled in a different version of Python may not always work 
properly. Use the same version for both pickling and unpickling.
3. Do not to unpickle data from an untrusted source. Malicious code inside the file might
be executed upon unpickling.
=========================================================================================
Not all pythons objects can be pickled;
https://www.datacamp.com/community/tutorials/pickle-python-tutorial
=========================================================================================
"""

template = {"id": 1, "random_int": [1010010101, 38294923443, 87475097572, 56030560364, 384527894572], "name": "Actor", "movies": ("Movie A", "Movie B"), "has_oscar": False, "country": "A Country", "created_date": datetime.now()}
dict_actor = [template for _ in range(100000)]
pickle_file = os.path.abspath(os.curdir) + os.sep + "src/storage/pickle_actor.pbin"
pickle_file_compression = os.path.abspath(os.curdir) + os.sep + "src/storage/pickle_actor.pbz2"
data_list: List[Dict[str, Any]]

# 1. Serializing / Pickling
# w=write, b=binary mode. The data will be written in the form of byte objects.
with open(pickle_file, "wb") as f:
    pickle.dump(dict_actor, f)

# 2. Deserializing / Unpickling
with open(pickle_file, "rb") as f:
    data_list = pickle.load(f)

print("Unpickling", data_list[0])

# 3. Serializing with compression
with bz2.BZ2File(pickle_file_compression, "wb", compresslevel=5) as f:
    pickle.dump(dict_actor, f)

# 4. Deserializing with compression
with bz2.BZ2File(pickle_file_compression, "rb", compresslevel=5) as f:
    data_list = pickle.load(f)

print("Unpickling Compression", data_list[0]) # just show first list

# Compare filesize
size_without_compression = os.path.getsize(pickle_file)
size_with_compression = os.path.getsize(pickle_file_compression)
# For smaller data, the size of compressed file can be larger than uncompression one
# Try change the comprehension template above from 1000 to 10 to see the difference
# For larger data above, the result 200437 (200KB) vs 304 bytes
print(f"Size Without vs With Compression {size_without_compression} vs {size_with_compression}")
