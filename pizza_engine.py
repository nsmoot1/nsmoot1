"""
ADD-100: Assignment 610A - The Resilient Pizza Engine
Author: Nick Smoot
Date: 3/20/26
File: pizza_engine.py
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[x] 1. Header Docstring included.
[x] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[x] 3. Function 'make_pizza' defines 4 specific parameters.
[x] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[x] 5. main() displays the Global Pantry list to the user.
[x] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# --- 1. Global constant ---

TOPPINGS = ("Pepperoni", "Sausage", "Bacon", "Pineapple")

# --- 2. Function definition ---

def make_pizza(customer, size, topping, is_delivery=False):
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")
    print(f"Delivery: {is_delivery}")


# --- 3. main() function ---

def main():
    print(f"Available Toppings: {TOPPINGS}")

    name = input("Enter your name: ")
    size = input("Enter size (Small, Medium, Large): ")
    topping = input("Enter topping: ")
    delivery = input("Is this delivery? (yes, no): ")

    try:
        if delivery == "yes":
            is_delivery = True
        else:
            is_delivery = False
    except Exception:
        print("Something went wrong, defaulting to pickup.")
        is_delivery = False


    make_pizza(
        customer=name,
        size=size,
        topping=topping,
        is_delivery=is_delivery
    )

main()