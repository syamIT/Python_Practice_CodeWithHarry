# def decorator (func):
#     print("Decorator Started from here : ");
#     def wrapper():
#         print("This function executes before the say_Hello function")
#         func()
#         print("This function executes after the say_Hello function")
#     return wrapper

# @decorator
# def say_Hello():
#     return "Hello From say_Hello function."
# res = say_Hello()
# print("Hello",res)
# say_Hello()

# # f = decorator(say_Hello)
# # f()


# Decorator is a function that takes a function and then 
# it creates a new function (wrapper),then it returns the new function

def decorators123(func):
    def wrapper():
        print("I am about to execute this function")
        func()
        print("I have executed this function")
    return wrapper


@decorators123
def sayHello():
    print("Hello...!!")
# sayHello()
f = decorators123(sayHello)
f()
'''
here f containts : 
def f():
    print("I am about to execute this function")
    print("Hello...!") #### which comes from sayHello function body
    print("I have executed this function")

'''

'''
f = decorators123(sayHello)
f()

this can be called as
'''
sayHello()
