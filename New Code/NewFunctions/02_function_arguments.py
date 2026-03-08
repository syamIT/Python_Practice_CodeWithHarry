# def add (a,b):
#     return a+b;
# print(add(12,50))



# Functions can take parameters and return values.
# Types of Arguments:
# 1. Positional Arguments
def add (a,b):
    return a+b;
print(add(12,50))


# 2. Default Arguments
def greet(name="Syam"):
    return f"Hello, {name}"
print(greet())

# 3. Keyword Arguments
def students(name,age,cls):
    return f"name = {name} and age = {age} and class is {cls}"
sd = students(name="Syam", age = 22, cls="A")
print("\nStudent Details : ",sd)