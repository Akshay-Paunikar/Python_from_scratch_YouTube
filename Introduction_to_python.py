"""
Introduction:

1) Python was created by Guido van Rossum and released in 1991. 
2) It is a high-level programming language that is widely used for web development, data analysis, artificial intelligence, scientific computing, and more. 
3) Python's design philosophy emphasizes code readability and simplicity, making it an excellent choice for beginners and experienced programmers alike.
4) Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It has a large standard library that 
provides many useful modules and functions, allowing developers to perform various tasks without needing to write code from scratch.
5) Python is an interpreted language, which means that code can be executed line by line, making it easier to test and debug. 
6) It also has a dynamic type system, allowing for flexibility in variable assignments and data structures.
7) Python has a strong community of developers who contribute to its growth and development. There are numerous resources available for learning Python, including online tutorials, 
documentation, and forums where users can ask questions and share knowledge.
8) Overall, Python's simplicity, versatility, and strong community support make it a popular choice for developers across various industries. Whether you're building web applications, 
analyzing data, or exploring artificial intelligence, Python provides the tools and resources needed to succeed.

"""

# writing your first python program
# This program will print "Hello, World!" to the console.
print("Hello, World!")

# variable assignment
# In Python, you can assign values to variables using the equals sign (=).
name = "Alice"
age = 30

# how to print variables/output
print(name)
print(age)

# Rules for variable names:
"""
1. Variable names must start with a letter or an underscore (_).
2. Variable names can contain letters, digits, and underscores.
3. Variable names cannot contain spaces or special characters.
4. Variable names are case-sensitive.
5. Variable names cannot be the same as reserved keywords in Python.

"""
# Example of valid variable names
my_variable = 10
print(my_variable)
_my_variable = 20
print(_my_variable)
myVariable1 = 30
print(myVariable1)

# Example of invalid variable names
# 1variable = 40  # Invalid: starts with a digit
# print(1variable)  # This will raise a syntax error

# Comments in Python:
"""
Comments are used to explain code and make it more readable. They are ignored by the Python interpreter.
Single-line comments start with the hash symbol (#) and can be placed on their own line or at the end of a line of code.
Multi-line comments can be created using triple quotes. They can span multiple lines and are often used for longer explanations or documentation.

"""
# Example of a single-line comment
# This is a single-line comment in Python.
# Multi-line comments can be created using triple quotes, as shown below.

"""
print("This is a multi-line comment in Python.")
print("It can span multiple lines and is often used for longer explanations or documentation.")

"""

'''
print("This is a multi-line comment in Python.")
print("It can span multiple lines and is often used for longer explanations or documentation.")

'''

# Various ways to print output in Python
# 1. Using the print() function
print("Hello, World!")  # Prints a string
print(42)  # Prints an integer

# 2. Using formatted strings (f-strings)
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")

# 3. Using the format() method
print("Name: {}, Age: {}".format(name, age))

# 4. Using the format() method with named placeholders to avoid confusion
print("Name: {name}, Age: {age}".format(name=name, age=age))

# Taking user input in Python
# The input() function is used to take input from the user. It always returns the input as a string, so you may need to convert it to the desired data type if necessary.
# Example of taking user input

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"Hello, {user_name}! You are {user_age} years old.")