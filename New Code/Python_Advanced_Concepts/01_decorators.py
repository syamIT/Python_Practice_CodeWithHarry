def decorator (func):
    print("Decorator Started from here : ");
    def wrapper():
        print("This function executes before the say_Hello function")
        func()
        print("This function executes after the say_Hello function")
    return wrapper

@decorator
def say_Hello():
    return "Hello From say_Hello function."
res = say_Hello()
print("Hello",res)
say_Hello()

# f = decorator(say_Hello)
# f()