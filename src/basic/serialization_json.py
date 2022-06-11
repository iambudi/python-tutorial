from datetime import datetime, date
import json
import os
from typing import Any, Callable

"""
=========================================================================================
Serialization is process of converting an object in memory to a byte stream 
that can be stored on disk or sent over a network. 
this character stream can then be retrieved and de-serialized back to a Python object
=========================================================================================
Json serialization|deserialization is quite stright forward in python, there are 2 methods
pass json string to json.loads() | json.dumps()
pass file pointer to json.load() | json.dump()
=========================================================================================
"""

# 1. Deserialization (Decode)
user = '{"id": 1, "name": "admin", "email":["admin@email.com", "admin2@email.com"], "active": true, "role": null}'
dict_user = json.loads(user)

# null will be converted as None
print("Json decoded to dict", dict_user)

# to parse json from file, use context manager and use json.load(f)
json_file = os.path.abspath(os.curdir) + os.sep + "src/storage/user.json"
with open(json_file, "r") as f:
    dict_user = json.load(f)

print("Json from file", dict_user)

# 2. Serialization (Encode)
# NOTE: datetime is not serializable so need to format as str first
created_date: datetime = datetime.strptime("2006-01-02 10:00:00", "%Y-%d-%m %H:%M:%S")
# or we can use a func and pass it to dumps(default=func)
# another alternative is using *jsonencoder* class and pass as dumps(cls=encoder_class)
default_handler: Callable[[Any], str | None] = lambda obj: obj.isoformat() if isinstance(obj, (date, datetime)) else None

dict_actor = {"id": 1, "name": "Actor", "movies": ("Movie A", "Movie B"), "has_oscar": False, "country": "A Country", "created_date": created_date}
print("Actor json encode", json.dumps(dict_actor, default=default_handler))
print("Pretty json encode", json.dumps(dict_actor, default=default_handler, indent=4, sort_keys=True))

# Using func handler can use pattern matching to handle different types
def handle_unserializable(json_val: Any) -> str | None:
    if isinstance(json_val, (date, datetime)):
        return json_val.isoformat()  # 2006-02-01T10:00:00
    return None


# Similiar to decode, to write json to file use dump()
with open(json_file, "w") as f:
    # make it pretty with indentation
    json.dump(dict_actor, f, indent=4, default=handle_unserializable)
