"""
AUTHOR: Nick Smoot
ASSIGNMENT: Assignment 4A: The Logic Gate
DATE: 2/09/2026
FILE: logic.py
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# --- 2. Ask the user for two integers ---

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# --- 3. Perform 6 logical checks ---

both_positive = num1 > 0 and num2 > 0
both_greater_than_100 = num1 > 100 and num2 > 100
either_even = num1 % 2 == 0 or num2 % 2 == 0
either_less_than_100 = num1 < 100 or num2 < 100
not_equal = num1 != num2
not_zero = num1 != 0 num2 != 0

# --- 4. Categorize number 1 ---

if num1 > 0:
    num1_category = "Positive"
elif num1 < 0:
    num1_category = "Negative"
else:
    num1_category = "Zero"

# --- 5. Print the results ---

print(f"Both numbers are greater than 0: {both_positive}")
print(f"Both numbers are greater than 100: {both_greater_than_100}")
print(f"Either number is even: {either_even}")
print(f"Either number is less than 100: {either_less_than_100}")
print(f"Numbers are not equal: {not_equal}")
print(f"Neither number is zero: {not_zero}")
print(f"The first number is categorized as: {num1_category}")

