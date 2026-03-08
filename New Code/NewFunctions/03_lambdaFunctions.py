#  Lambda Functions in Python
# Lambda functions are anonymous, inline functions.

# square = lambda x: x**2
# print(square(5))
# XOR = lambda y: y^2
# print(XOR(5))

'''
As goog as this : 
def sub(z,y,z=10):
    return x+y-z;
'''
sub = lambda x,y,z=10: x+y-z;
print(sub(1,20,5));