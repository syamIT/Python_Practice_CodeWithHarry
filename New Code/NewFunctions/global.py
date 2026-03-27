# def sum(a,b):
#     c = a+b;
#     return c;
# c = 100; #global variable which is constant
# print(c)
# print(sum(100,12))




def sum(a,b):
    global c; #accessing global variable c inside a local function, Now this variable can be modified with this function.
    c = a+b; # global variable c is modifying here.
    return c;
c = 100; #global variable which is constant
print(c)
print(sum(100,12))
print(c)




