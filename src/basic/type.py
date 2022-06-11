from typing import Dict, List, NewType, Tuple

"""
#############################################################
Type Alias.
It's like var assigment but with typehint rather than value
#############################################################
"""
Connection = Dict[str, str]
Server = Tuple[str, Connection]

# here Server as a type hint, not a type like NewType
# when run() called, pass value of tuple[str, dict]
# not Server(str, Connection)
def run(server: Server):
    print(f"{server[0]} server on {server[1]['address']}:{server[1]['port']} is ready")


run(("local", {"address": "0.0.0.0", "port": "80"}))

"""
#############################################################
NwType
Python allow for creating new distinct Types 
Use helper class NewType from typing
#############################################################
"""

# To prevent ambiguity between a new type or function
# use CamelCase: Role("") vs role("")
Role = NewType("Role", str)
Permission = NewType("Permission", str)
# NewType can also be derived from another NewType
# But vscode type checking will tell it's compatible when assign str to Permission
# It means better use literal type directly rather than derived type
# Permission = NewType("Permission", Role)

admin = Role("admin")
editor = Role("editor")

perm_create = Permission("article.create")
perm_view = Permission("article.view")
perm_delete = Permission("article.delete")


def assign_permission_to(role: Role, permissions: List[Permission]):
    print(f"Role {role} has permissions: {permissions}")
    pass


assign_permission_to(admin, [perm_create, perm_view, perm_delete])
assign_permission_to(editor, [perm_create, perm_view])

# Type operation on variable type NewType can be performed
# But the result type will be original not NewType
# Following should return type 'str' not 'Role'
roles = admin + editor
print(f"Type of admin + editor {roles} is {type(roles)}")
