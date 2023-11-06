"""
Task: Define a function sayhi(n, msg) that:

1. n is by default 1, if user doesn't pass an argument to the function.
2. msg by default is 'Welcome to Python Functions', if user doesn't pass an argument.
3. print msg n times.
"""

def sayhi(n = 1, msg = "Welcome to Python Functions"):
  for i in range(n):
    print(msg)

#sayhi(0)
#sayhi(1)
#sayhi(5)
#sayhi(3, "yeah")
