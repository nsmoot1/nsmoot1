"""
ADD-100: Assignment 6B - The Locked Calendar
Author: Nick Smoot
Date: 2/23/2026
File: locked_calendar.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.
-----------------------------------------------------------------------
"""

# --- 1. MONTHS is defined as a constant tuple () ---

MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

# --- 2. Loop to display each month ---

print("Months of the year:")
for month in MONTHS:
 print(f"{month:<10}")

# --- 3. 'try' and 'except' blocks catch a TypeError ---
try:
    MONTHS[0] = "Jan"
except TypeError as e:

    # --- 4. Explain why the modification failed ---

    print("\nError: Cannot modify MONTHS because it is a tuple, which is immutable.")
    print("Tuples do not support item assignment, so this operation is not allowed.")
    print(f"TypeError message: {e}")



    
