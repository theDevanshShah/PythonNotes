
# Lesson on Variables in Python

# Variables are used to store data that can be used later in the program.
# In Python, you don't need to declare the type of variable, you just assign a value to it.

# Example of different types of variables:

# Integer
age = 25
print("Age:", age)

# Float
height = 5.9
print("Height:", height)

# String
name = "John Doe"
print("Name:", name)

# Boolean
is_student = True
print("Is Student:", is_student)

# You can also change the value of a variable after it has been assigned
age = 26
print("New Age:", age)

# Variables can be used in expressions
years_to_graduate = 4
graduation_age = age + years_to_graduate
print("Graduation Age:", graduation_age)

# You can also assign multiple variables in one line
x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)

a,b,c,= 4,5,6
print("a:", a, "b:", b, "c:", c)

# Variables can be reassigned to different types
x = "Now I'm a string"
print("x:", x)

# Remember, variable names should be descriptive and follow the naming conventions
# They should start with a letter or underscore, and can contain letters, numbers, and underscores
# Examples of valid variable names: my_variable, variable1, _variable
# Examples of invalid variable names: 1variable, variable-name

# That's it for the basics of variables in Python!

# Variable methods in Python

# Strings have many useful methods
greeting = "hello world"
print("Uppercase:", greeting.upper())
print("Capitalize:", greeting.capitalize())
print("Replace:", greeting.replace("world", "there"))
print("Split:", greeting.split())

# my example for strings
someWord = "Hello Devansh"
print(someWord)
print("Uppper Case : ", someWord.upper())
print("Capitalize : ", someWord.capitalize())
print("Replace : ", someWord.replace("Devansh", "Dev"))
print("Split : ", someWord.split())
print("Split Line : " , someWord.splitlines()) # expecting ['Hello Devansh']
print("For counting a specific character's occurance ",someWord.count('l'))
print(someWord.endswith('h')) # expecting true
print(someWord.endswith('d')) # expecting false
print(someWord.startswith('H')) # expecting true
print(someWord.startswith('h')) # expecting false
print(someWord.format('Devanshi')) # expecting Hello Devansh
print(someWord.index('D')) # expecting 6