def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in  range(n):
                result = func(a)
                print(f"Result {i+1} : ,{result}")
        return wrapper
    return decorator

@repeat(10)
def Greeting(name):
    return ( f"Good Morning...!!! {name}")
Greeting("Syam")
