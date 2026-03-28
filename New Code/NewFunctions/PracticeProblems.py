# 1. Defining Functions

# Write a function greet() that prints "Hello, Python Learner!" when called.

# def greet():
#     print("Hello, Python Learner!");
# greet()

# Write a function square(num) that returns the square of a given number. Test it with different numbers.

# def square(num):
#     return num*num;
# print(square(21))


# 2. Function Arguments & Return Values
# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

# def full_name(fir, last):
#     return fir+' '+last;
# print(full_name('syam','prasad'))

# def fullName(first, last):
#     return f"{first} {last}";
# print("Full Name : ",fullName("Syam","Venni"))



# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)

# def calculate_area(length, width=10):
#     return length*width;
# print(calculate_area(16))


# 3. Lambda Functions
# Write a lambda function that adds two numbers and test it.
# sum = lambda a,b: a+b;
# print("Sum : ",sum(2,2));


# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
# mapnum = [1, 2, 3, 4, 5];
# res = list(map(lambda x: x**2, mapnum))
# print("Result : ",res)


# Write a recursive function Factorail(n) that returns the fibanacci of a number.
# def factorial(n):
#     if(n==1 or n== 0): return 1;
#     return n * factorial(n-1);
# factorialRes = factorial(5)
# print(factorialRes)




# Write a recursive function fibanacci(n) that returns the fibanacci of a number.

# 4. Recursion in Python
# Write a recursive function fibanacci(n) that returns the fibanacci of a number.
# fibanacci series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
# def fibanacci(n):
#     if(n == 1 or n == 0): 
#         return n;
#     return fibanacci(n-1) + fibanacci(n-2);
# print(fibanacci(15));

# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.

# def sum_of_digits(n):
#     if(n<10): return n;
#     else: all_but_last, last = n//10, n%10;
#     return sum_of_digits(all_but_last) + last;
# print(sum_of_digits(129))
# print(129//10)
# print(129%10)




# 5. Modules and Pip – Using External Libraries
# Import the math module and use it to:

# Find the square root of 144
# import math as mt;
# print(mt.sqrt(144))

# Calculate sin(90°) (hint: use math.radians())
# print(mt.tan(mt.radians(45)))




# 2. Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".   

# import requests as r;
# print(r.get('https://api.github.com'))

# import requests

# Send a GET request to the GitHub API
# response = requests.get('https://api.github.com')
# print(response.text)
# print("Status Code:", response.status_code)
# print("Response current_user_url:", response.json()['current_user_url']);








# 6. Variable Scope and Docstrings
# 1. Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
# def increment():
#     counter = 0;
#     counter = counter+1
#     return counter;
# print(increment())
# print(increment())
# print(increment())



# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

# def multiply(a,b):
#     ''' This function results product of a and b
#         a is first Number (int)
#         b is second number (int)
#         this returns a*b as a result.
#     '''
#     return a*b;
# help(multiply(31,2))








# 7. Bonus Challenges
# 1. Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.



# 7. Bonus Challenges
# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

# def safe_divide(a,b):
#     if(b == 0): return f"Cannot divide by Zero"
#     return a/b;
# print(safe_divide(10,10))


# Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
import my_utils as mu;
print(mu.is_even(0.2323))

