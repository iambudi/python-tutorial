"""
Hello World!
This is how to write multiline comments
by using triple double quotes
"""

print("Hello World")
# int can't be concatenated with string
print(int("1") + 2)

# var assignment
a = 10
# typhinting annotation is just guidance not enforced
# Its benefit for the linter or type checking not at runtime
a: int = 10
# so here we can still allowed to assign string to a
# turn off vscode typechecking to validate this is okay
# a = "Hello World"
# assignment expression in branching or while loop using :=
if status := (a * 2) > 1:
    print("a > 1 is ", status)

# Python has 4 primitive data types
print(f"A = {type('A')} ", f"10 = {type(10)}", f"10.1 = {type(10.1)}", f"True = {type(True)}")

# use bracket for scoping condition
while (number := input("Enter a number, 0 to stop: ")) != "0":
    print("You keyed in:", number)

# multi var assignment from tuple
user, admin, it = ("user", "admin", "IT")
print(user, admin, it)

# Math operation
a = 1 + 5
b = a * a
c = b - a / 1.5
print("c type is ", type(c))
# Specify separator between print args and end of print value
print("a", a, "b", b, "c", c, sep=", ", end="======\n")
# var switching
a, b = b, a
print("Switch vars", a, b)


# String interpolation and formatting
dictionary = {"name": "Python", "age": 10}
# using print placeholder
print("name %s, age %d" % (dictionary["name"], dictionary["age"]))
# using string format()
print("Each value of a,b and c is {}, {}, {}".format(a, b, c))
# using fstring
print(f"Expression inside string 10 + 10 = {10+10}")
print(f"Dict value is {dictionary}")




