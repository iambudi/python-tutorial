import re

"""
Refer doc
https://docs.python.org/3/library/re.html
"""

# Get version string
m = re.search(r"\d+\.\d+\.\d*", "python 3.10.0 latest update on Oct 4th 2021")
print(m.group(0) if m is not None else None)
