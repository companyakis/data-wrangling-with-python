"""
Task: Dedine a function sayhi() that:

Ask user for an int and save it to n .
print 'Welcome to Python Functions' n times

Task: Call sayhi()

"""

def sayhi():
  n = input("A number please: ") 
  n = int(n)
  for i in range(n):
    print("Welcome to Python Functions")
   
sayhi()
