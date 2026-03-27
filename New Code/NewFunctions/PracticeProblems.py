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



# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)

# def calculate_area(length, width=10):
#     return length*width;
# print(calculate_area(16))


# 3. Lambda Functions
# Write a recursive function factorial(n) that returns the factorial of a number.



# 4. Recursion in Python
# Write a recursive function factorial(n) that returns the factorial of a number.
# factorial series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
# def factorial(n):
#     if(n == 1 or n == 0): 
#         return n;
#     return factorial(n-1) + factorial(n-2);
# print(factorial(15));

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

import requests

# Send a GET request to the GitHub API
response = requests.get('https://api.github.com')
print(response.text)
print("Status Code:", response.status_code)
print("Response current_user_url:", response.json()['current_user_url']);