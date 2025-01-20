import traceback

# Strings in python

# Strings are immutable in python
# Strings are sequences of characters
# Strings are ordered sequences
# Strings are iterable
# Strings can be indexed

# String Methods
string = "   Here I am Typing Some String With All The Mix Cases Of UPPER And lower.   "

# 1. lower() - converts all characters in the string to lower case
print("Lower :", string.lower())

# 2. upper() - converts all characters in the string to upper case
print("Upper : ", string.upper())

# 3. capitalize() - converts the first character of the string to upper case
print("Capitalize :",string.capitalize())

# 4. title() - converts the first character of each word in the string to upper case
print("Title :", string.title())

# 5. swapcase() - converts all upper case characters to lower case and vice versa
print("SwapCase :", string.swapcase())

# 6. strip() - removes leading and trailing whitespaces
print("Strip : ",string.strip())

# 7. lstrip() - removes leading whitespaces
print("Lstrip : ",string.lstrip())

# 8. rstrip() - removes trailing whitespaces
print("Rstrip : ",string.rstrip())

# 9. split() - splits the string into a list of substrings based on a delimiter
print("Split :", string.split())

# 10. join() - joins a list of strings into a single string
print("Join : ", string.join(["1", "2", "3"]))

# 11. replace() - replaces a substring with another substring
print("Replace : ", string.replace("UPPER", "Lower"))

# 12. find() - finds the index of the first occurrence of a substring
print("Find : ", string.find("UPPER"))

# 13. rfind() - finds the index of the last occurrence of a substring
print("RFind : ", string.rfind("I")) # If the string got whatever you are looking for, it will return the index number of last occurance
print("RFind : ", string.rfind("Z")) # If the string not got whatever you are looking for, it will return -1

# 14. index() - finds the index of the first occurrence of a substring
print("Index : ", string.index("U"))

# 15. rindex() - finds the index of the last occurrence of a substring
print("R-Index : ", string.rindex("R"))

# 16. count() - counts the number of occurrences of a substring
print("Count : ", string.count("i"))

# 17. startswith() - checks if the string starts with a given substring
print("Starts With : ", string.startswith(" ")) # For True Case
print("Starts With : ", string.startswith("U")) # For False Case

# 18. endswith() - checks if the string ends with a given substring
print("Ends With : ", string.endswith(" ")) # For True Case
print("Ends With : ", string.endswith("U")) # For False Case

# 19. isalnum() - checks if the string is alphanumeric
alphanumericString = "ABCD123"
print("Is Alpha Numeric : ", alphanumericString.isalnum())

# 20. isalpha() - checks if the string is alphabetic
onlyAlphabeticString = "ABCD"
print("Only Alphabetic String : ", onlyAlphabeticString.isalpha())

# 21. isdigit() - checks if the string is numeric
onlynumericString = "123"
print("Only Numeric String : ", onlynumericString.isdigit())

# 22. islower() - checks if the string is in lower case
onlyLowerString = "hello from dev!"
print("If the string is only lower : ", onlyLowerString.islower())

# 23. isupper() - checks if the string is in upper case
onlyUpperString = "HELLO FROM DEV!"
print("If the string is only in upper : ", onlyUpperString.isupper())

# 24. isspace() - checks if the string is whitespace
stringWithWhiteSpace = "   "
print("Is WhiteSpace : ", stringWithWhiteSpace.isspace()) # For True Case
print("Is WhiteSpace : ", string.isspace()) # For False Scenario

# 25. isidentifier() - checks if the string is a valid identifier
identifierString = "validIdentifier"
print("Is Identifier : ", identifierString.isidentifier()) # For True Case
invalidIdentifierString = "123Invalid"
print("Is Identifier : ", invalidIdentifierString.isidentifier()) # For False Case

# 26. isprintable() - checks if the string is printable
printableString = "This is printable!"
print("Is Printable : ", printableString.isprintable()) # For True Case
nonPrintableString = "This is not printable!\n"
print("Is Printable : ", nonPrintableString.isprintable()) # For False Case

# 27. isascii() - checks if the string is ASCII
asciiString = "This is ASCII!"
print("Is ASCII : ", asciiString.isascii()) # For True Case
nonAsciiString = "This is not ASCII! 😊"
print("Is ASCII : ", nonAsciiString.isascii()) # For False Case

# Exception Handling In Python
# try, except, else, finally

# try block - contains the code that might raise an exception
# except block - contains the code that handles the exception
# else block - contains the code that is executed if the try block does not raise an exception
# finally block - contains the code that is always executed

# Example

var1 = int(input("Enter the first number: "))
var2 = int(input("Enter the second number: "))

try:
    result = var1/var2
    print("Var1 Divided By Var2 = ",result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
    traceback.print_exc()
except ValueError:
    print("Invalid input!")
    traceback.print_exc() 
except Exception as e:
    print("An error occurred! {e}")
    traceback.print_exc()
else:
    print("Division successful!")
finally:
    print("Execution completed!")
   
 # __________________________________________________________________________________________________________________________________________________________________________________________________________________
 
''' 
 DATA STRUCTURES IN PYTHON
 
   1. List
   List is a collection of items / values which is
   -> Ordered   ( Maintains the insertion order)
   -> Changable ( Can be changed after creating them)
   -> Can Be Duplicate
   -> It is written with square brackets
'''   
# Playing with lists in python

myFirstList = [10,10.5,"Pizza"]
# Examples of different types of lists with descriptive names
numbers_list = [1, 2, 3, 4, 5, 6, 7, 1.2, 1.3, 4.5, 6.7, 5.5]
chars_list = ['a', 'b', 'c', 'A', 'B', 'C']
strings_list = ['Abc', 'ABC', 'abc']
mixed_data_list = [True, 5.5, '5.5', 'True', False, 143]

mainList = [1,2,3,4,5,6,7,8,9,10,"Dev","Data","Science"]

if "Dev" in mainList:
    print("Dev is in the list")
else:
    print("Dev is not in the list")
    
    
if "Devansh" in mainList:
    print("Devansh is in the list")
else:
    print("Devansh is not in the list")
    
    
# Accessing elements of a list

# 1. Accessing elements using positive indexing
print(mainList[0]) # 1
print(mainList[1]) # 2
print(mainList[2]) # 3
print(mainList[3]) # 4
print(mainList[4]) # 5

# 2. Accessing elements using negative indexing (Reverse Indexing)
print(mainList[-1]) # 10
print(mainList[-2]) # 9
print(mainList[-3]) # 8
print(mainList[-4]) # 7
print(mainList[-5]) # 6

'''
Now here in negative indexing,
it will become easier if we use len() 
as we have mainList[] here
if i want to access mainList[-1] then
i can also visualize it in this way print(mainList(len(mainList)-1))
'''

# Slicing a list
print(mainList[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Dev', 'Data', 'Science']
print(mainList[0:5]) # [1, 2, 3, 4, 5]
print(mainList[5:]) # [6, 7, 8, 9, 10, 'Dev', 'Data', 'Science']
print(mainList[:5]) # [1, 2, 3, 4, 5]
print(mainList[-5:]) # [6, 7, 8, 9, 10, 'Dev', 'Data', 'Science']
print(mainList[:-5]) # [1, 2, 3, 4, 5, 6, 7, 8]

# Changing elements of a list
mainList[0] = 100
print(mainList) # [100, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Dev', 'Data', 'Science']

# List comprehension
# List comprehension is a concise way to create lists on to go
# Syntax: [expression for item in iterable if condition]

# Example

basicList = [i for i in range(10)]
print(basicList)

basicList2 = [i**i for i in range(10)]
print(basicList2)

basicList3 = [i for i in range(10) if i%2==0]
print(basicList3)

# listOfSquares = [i**2 for i in range(1, 11)]
# print(listOfSquares)

# List Methods

list1 = [1,2,3,4,5]
print(list1)


# 1. append() - adds an element to the end of the list
list1.append("Python")
print(list1)

