# ===========================
# Loops in Python: While Loop
# ===========================

# Loops are like DJs—they repeat the beat until you tell them to stop (or something stops them)!

# -------------------------------------------------------------
# 1. While Loop: The Endless Repeater (if you're not careful)
# -------------------------------------------------------------

# Basic Example: Counting up
count = 1
while count <= 5:  # As long as count is less than or equal to 5
    print("Count is:", count)  # Print the count
    count += 1  # Increment count by 1

# Basic Example: Counting down
count = 5
while count >= 1:  # As long as count is greater than or equal to 1
    print("Count is:", count)
    count -= 1  # Decrement count by 1

# -------------------------------------------------------------
# 2. Print numbers from 1 to 100
# -------------------------------------------------------------
count = 1
while count <= 100:  # Python can count to infinity (but your patience won't last)
    print(count)
    count += 1  # Shorthand for count = count + 1

# -------------------------------------------------------------
# 3. Multiplication Table (a classic!)
# -------------------------------------------------------------
n = int(input("Enter a number: "))
count = 1
while count <= 10:  # Multiplying from 1 to 10
    print(n, "x", count, "=", n * count)
    count += 1

# -------------------------------------------------------------
# 4. Print squares of numbers from 1 to 10
# -------------------------------------------------------------
count = 1
while count <= 10:
    print("Square of", count, "is:", count * count)
    count += 1

# -------------------------------------------------------------
# FUN & WEIRD THINGS ABOUT LOOPS
# -------------------------------------------------------------

# 1. The "Infinite Loop of Doom":
# If you forget to increment the counter, the loop will run forever! 
# Example (DO NOT RUN THIS UNLESS YOU LIKE CHAOS):
# while True:
#     print("Oops! I forgot to stop!")

# 2. Breaking the Loop:
# Use the "break" statement to exit a loop prematurely.
print("\nBreaking the loop after finding an even number:")
count = 1
while count <= 10:
    if count % 2 == 0:  # Check for even numbers
        print("Found an even number:", count)
        break  # Stop the loop
    count += 1

# 3. Skipping to the Next Iteration:
# Use "continue" to skip the rest of the code for a particular iteration.
print("\nSkipping odd numbers:")
count = 1
while count <= 10:
    if count % 2 != 0:  # Check for odd numbers
        count += 1
        continue  # Skip the print statement
    print("Even number:", count)
    count += 1

# -------------------------------------------------------------
# INTERESTING PROGRAMS TO TRY
# -------------------------------------------------------------

# 1. Reverse the digits of a number (without using strings)
print("\nReversing the digits of a number:")
number = int(input("Enter a number to reverse: "))
reversed_num = 0
while number > 0:
    digit = number % 10  # Extract the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    number //= 10  # Remove the last digit
print("Reversed number is:", reversed_num)

# 2. Sum of digits of a number
print("\nCalculating the sum of digits:")
number = int(input("Enter a number: "))
digit_sum = 0
while number > 0:
    digit_sum += number % 10  # Add the last digit to the sum
    number //= 10  # Remove the last digit
print("Sum of digits is:", digit_sum)

# 3. Guessing Game (A little fun!)
import random
target = random.randint(1, 10)  # Random number between 1 and 10
attempts = 0
print("\nGuess the number between 1 and 10!")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == target:
        print("Congratulations! You guessed it in", attempts, "attempts.")
        break
    elif guess < target:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# 4. Check if a number is a palindrome
print("\nCheck if a number is a palindrome:")
number = int(input("Enter a number: "))
original_number = number
reversed_num = 0
while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10
if original_number == reversed_num:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")

# -------------------------------------------------------------
# BONUS TIPS: Loops in Python vs Other Languages
# -------------------------------------------------------------

# 1. Python has no "do-while" loop like some other languages. 
#    But you can mimic it like this:
print("\nMimicking a do-while loop:")
count = 1
while True:
    print("Count is:", count)
    count += 1
    if count > 5:
        break

# 2. Loops can be nested! (but don't go overboard or you'll confuse yourself):
print("\nNested loops example:")
rows = 3
cols = 3
row = 1
while row <= rows:
    col = 1
    while col <= cols:
        print(f"({row}, {col})", end=" ")
        col += 1
    print()
    row += 1

# -------------------------------------------------------------
# THE GOLDEN RULE OF LOOPS: Avoid Infinite Loops Unless You're Doing It On Purpose!
# -------------------------------------------------------------
# Infinite loops are useful in things like server applications, games, or any program 
# that needs to keep running indefinitely.