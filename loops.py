"""
-----------------------------------------------------------------------
AUTHOR: Nick Smoot
ASSIGNMENT: 4B - Loops
DATE: 2/09/2026
FILE: loops.py
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""






# --- 1: Nagging Kid Loop ---

nagging = True  # Boolean variable to control the loop  
while nagging:
    response = input("Are we there yet? ")
    if response.lower() == "yes":
        nagging = False  # Exit the loop when user types "yes"

# --- Task 2: For Loop (99 Bottles of Beer) ---

for bottles in range(99, 0, -1):  # Counts backwards from 99 to 1
    print(f"{bottles} bottles of beer on the wall!")