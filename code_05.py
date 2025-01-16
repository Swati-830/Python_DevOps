"""def greet(name):
    print(f"Hello {name}")

greet("Tushar")
greet("Swati")"""



"""def addition(a,b):
    return a+b

print(addition(10,20))

print(addition(12,20))"""

"""def is_even(num):
    return num%2==0

def is_odd(num):
    return num%2!=0

def square(num):
    return num**2

# Test the functions

num =int(input("Enter a number: "))

if is_even(num):
    print(f"{num} is even")
else:    
    print(f"{num} is odd")  
    
print(f"Square of {num} is {square(num)}")"""



import math_op

a = math_op.add(10,20)
print(a)

a = math_op.subtract(100,20)
print(a)

print(f"The substraction of 100 and 20 is {math_op.subtract(100,20)}")

x = int(input("Enter a number: "))
y= int(input("Enter a number: "))

b= math_op.multiply(x,y)
print(b)