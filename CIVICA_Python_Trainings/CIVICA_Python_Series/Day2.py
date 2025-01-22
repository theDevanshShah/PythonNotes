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

# Local Variables Vs Global Variables

# Variables that are defined inside a function are LOCAL variables
# Example

def  method_one():
    num1 = 10
    print("Inside method_one:", num1)
    
# def method_two():
#    print("Inside method_two:", num1) # this will not run & it will give compile time error
    
method_one()
# method_two()

# Variables that are defined outside a function are GLOBAL variables
# Example

num2 = 20
def method_three():
    print("Inside method_three:", num2)

def method_four():
    print("Inside method_four:", num2)
    
method_three()
method_four()

# Now we can do the same in different method

def method_five():
    global num3
    num3 = 30
    print("Inside method_five:", num3)
    
def method_six():
    print("Inside method_six:", num3)
    
method_five()
method_six()

# Type Casting

# 1. int to float
inum = 10
fnum = float(inum)

print("Before Type Casting:", inum," is of type", type(inum))
print("After Type Casting:", fnum," is of type", type(fnum))

# 2. float to int
fnum2 = 10.122
inum2 = int(fnum2)
print("Before Type Casting : ",fnum2 ,"is type of ",type(fnum2))
print("After Type Casting :",inum2," is type of ",type(inum2))

# 3. int to string
inum3 = 13
string1 = str(inum3)
print("Before Casting : ",inum3,"is type of ",type(inum3))
print("After Type Casting ",string1,"is type of ",type(string1))

# 4. string to int
string2 = "123"
inum4 = int(string2)
print("Before Type Casting : ",string2," is the type of : ",type(string2))
print("After Type Casting ",inum4,"is the type of : ",type(inum4))

# 5. int to boolean
inum5 = 20
bool1 = bool(inum5)
print("Before Type Casting : ",inum5," is the type of :", type(inum5))
print("Before Type Casting : ",bool1," is the type of :", type(bool1))


# 6. Boolean to into int
boolean1 = True
inum6 = int(boolean1)
print("Before Type Casting : ",boolean1,"is the type of :",type(boolean1))
print("After Type Casting :  ",inum6,"is the type of :",type(inum6))

# Handling User Input

# When The Input Type Is String
stringValue = input("Enter some string: ")
print("You entered: ", stringValue)

# When The Input Type Is Integer
intValue = int(input("Enter some integer: "))
print("You entered: ", intValue , "which is type of ",type(intValue))

# When the Input type is float
floatValue = float(input("Enter some float: "))
print("You entered: ", floatValue , "which is type of ",type(floatValue))

# When the input type is boolean
boolValue = bool(input("Enter some boolean value here : "))
print("You have entered : ", boolValue , "which is type of ",type(boolValue))

# Operators in python

# 1. Arithmetic Operators
num1 = 10
num2 = 5

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2
floorDivision = num1 // num2

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Modulus:", mod)
print("Exponent:", exp)
print("Floor Division:", floorDivision)

# 2. Comparison Operators

num3 = 10
num4 = 5

print("Equal:", num3 == num4)
print("Not Equal :", num3 != num4)
print("Greater Than : ", num3 > num4)
print("Less Than : ", num3 < num4)
print("Greater Than Or Equal To : ", num3 >= num4)
print("Less Than Or Equal To : ", num3 <= num4)

# 3. Logical Operators

bool1 = True
bool2 = False

print("AND:", bool1 and bool2)
print("OR:", bool1 or bool2)
print("NOT:", not bool1)

# 4. Assignment Operators

num5 = 10
num5 += 5
print("Addition Assignment:", num5)

num5 -= 5
print("Subtraction Assignment:", num5)

num5 *= 5
print("Multiplication Assignment:", num5)

num5 /= 5
print("Division Assignment:", num5)

num5 %= 5
print("Modulus Assignment:", num5)

num5 **= 5
print("Exponent Assignment:", num5)

# 5. Identity Operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("Is:", x is z)
print("Is Not:", x is not y)

# same example but with different values

a = 10
b = 5
c = a
print("Is : ",a is c)
print("Is Not : ",a is not b)

# 6. Membership Operators

fruits = ["apple", "banana"]

print("In:", "apple" in fruits)
print("Not In:", "orange" not in fruits)
print("In:", "bananaa" in fruits)
print("Not In:", "banana" not in fruits)