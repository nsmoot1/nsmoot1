"""
-----------------------------------------------------------------------
AUTHOR: Nick Smoot
ASSIGNMENT: 3B - The Buffet Calculator
DATE: 2/02/2026
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

# --- 1. Ask the user for their age ---

age = int(input("Enter your age.: "))

# --- 2. Determine price ---

if age < 1:
    price = 0.00
elif 1 <= age <= 11:
    price = age * 1.00
elif 12 <= age <= 64:
    price = 16.95
else:  # age 65 and older
    price = 12.95

# --- 3. Print the final price ---

print(f"The final price is: ${price:.2f}")


