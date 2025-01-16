# Python_DevOps

Python 1991 Guido van Rossum 

high level 
versatile
dynamically typed

## Key features
1. Easy to read and learn
2. Multipurpose  
3. Interpreted language
4. Rich standard library 
5. Platfrom independent 
6. large community and ecosystem

1. Easy to Read and Learn
Python is simple and looks like plain English. This makes it easy to learn for beginners.
Example:
print("Hello, World!")


2. Multipurpose
You can use Python for many things, like:

Building websites (e.g., with Django or Flask).
Data analysis and creating charts.
Making games or simple programs.
Automating repetitive tasks, like renaming files.


3. Interpreted Language
You don’t need to compile Python code. Just write it and run it directly.
Example:

x = 5
y = 10
print(x + y)  # Output: 15


4. Rich Standard Library
Python comes with many built-in tools, so you don’t have to start from scratch.
Example:

math for calculations.
datetime for working with dates and times.

import math
print(math.sqrt(9))  # Output: 3.0

5. Platform Independent
You can run Python on any computer (Windows, Mac, or Linux) without changing the code.

6. Large Community and Ecosystem
Millions of people use Python, so you’ll find lots of help, tutorials, and ready-made tools for almost anything.

comment
variables
## Data types
1. Numeric Data types
x=123
y=1.234

2. String
a= 'Swati'
b= "Tushar"

s= '''this is my aditya's
    swati
    swati'''

3. Boolean Data type
is_valid = true
has_permission = false

4. list 
a= [1,2,3, 'Adi' , true]
    0 1 2   3       4

mutable
a[0] =1
a[0]=6
[6,2,3, 'adi' true]

5. Tuple
Immutable
b= (1,2,3, 'adi' ,true)

6. Dictonaries
my_dict ={'name':'John' , 'age':30, 'city':'New York'}

print(my_dict[name]) ---> John


7. Set
my_set = {1,2,3,2,3,3,3,5,5,3,4,4,4}
print(my_set) ---> {1,2,3,4,5}

## Data Types
1. Numeric Data Types
Numeric data types in Python store numbers:

int: For whole numbers (e.g., 123)
float: For decimal numbers (e.g., 1.234)
Example:


x = 123       # Integer
y = 1.234     # Float
print(x, y)   # Output: 123 1.234


2. String
Strings are used to store text.

You can use single (') or double (") quotes for simple strings.
Triple quotes (''' or """) are used for multi-line text.
Example:

a = 'Swati'              # Single quotes
b = "Tushar"             # Double quotes

s = '''this is my aditya's
    swati
    swati'''             # Multi-line string
print(s)


3. Boolean Data Type
Booleans represent True or False values. They’re used for conditions or flags.
Example:

is_valid = True          # True
has_permission = False   # False
print(is_valid)          # Output: True


4. List
Lists store multiple values in order, and you can mix different data types.

Indexing starts from 0.
Mutable: You can change values in a list.
Example:

a = [1, 2, 3, 'Adi', True]  # List with mixed types
print(a[3])                 # Output: 'Adi'

Modifying the list
a[0] = 6
print(a)                    # Output: [6, 2, 3, 'Adi', True]
5. Tuple
Tuples are like lists but are immutable, meaning their values cannot be changed after creation.
Example:

b = (1, 2, 3, 'Adi', True)  # Tuple with mixed types
print(b[3])                 # Output: 'Adi'

 b[0] = 6  # This will cause an error since tuples are immutable


6. Dictionaries
Dictionaries store data in key-value pairs.

Keys are unique, and you can use them to access values.
Example:

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['name'])      # Output: John


7. Set
Sets store unique values only, meaning duplicates are automatically removed.

They are unordered, so there’s no indexing.
Example:

my_set = {1, 2, 3, 2, 3, 3, 5, 5, 3, 4, 4, 4}
print(my_set)              # Output: {1, 2, 3, 4, 5}


