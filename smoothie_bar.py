"""
ADD-100: Assignment 9A - The Smoothie Sprint
Author: Nick Smoot
Date: 3/16/2026
File: smoothie_bar.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. Global Constants BASES and FRUITS defined as Tuples.
[x] 3. Professional function get_price(size) returns a float.
[x] 4. Professional function blend(size, base, fruit, scoops) for output.
[x] 5. main() function handles try/except for scoops (int).
[x] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")

# --- GET PRICE FUNCTION ---

def get_price(size):
    if size == "Small":
        return 3.00
    elif size == "Medium":
        return 4.00
    else:
        return 5.00
    
# --- BLEND FUNCTION ---

def blend(size,base,fruit,scoops):
    print("\n--- Blending Smoothie ---")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit} ({scoops} scoops)")

# --- MAIN FUNCTION ---

def main():
    print("Welcome to Nicks Smoothie Bar!")

    choice_size = input("Size (Small/Medium/Large): ").title().strip()
    choice_base = input("Base (Water/Apple Juice/Orange Juice/Milk): ")
    choice_fruit = input("Fruit (Strawberry/Banana/Mango/Blueberry): ")
    try:
        scoops = int(input("How many scoops of fruit? "))
    except ValueError:
        print("Invalid entry. Defaulting to 1 scoop.")
        scoops = 1

    price = get_price(choice_size)
    blend(choice_size, choice_base, choice_fruit, scoops)
    print(f"Total Bill: ${price:.2f}")

main()