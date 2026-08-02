# In Python, try and except are used for exception handling, allowing your program to handle errors gracefully instead of crashing.

try:
    # Code that may cause an exception
    x = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("You cannot divide by zero.")